import pandas as pd
import numpy as np
import os
import sys
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_ob_dir_path: str = os.path.join('artifacts', 'preprocessor')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def get_data_transformer_object(self):
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender", "race_ethnicity", "parental_level_of_education", "lunch", "test_preparation_course",
            ]

            num_pipeline = Pipeline([
                ("imputer", SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())
            ])
            logging.info("Numerical columns scaling pipeline created")

            cat_pipeline = Pipeline([
                ("imputer", SimpleImputer(strategy='most_frequent')),
                ('one_hot_encoder', OneHotEncoder()),
                ("scaler", StandardScaler(with_mean=False))
            ])
            logging.info("Categorical columns encoding pipeline created")

            preprocessor = ColumnTransformer([
                ("num_pipeline", num_pipeline, numerical_columns),
                ("cat_pipeline", cat_pipeline, categorical_columns)
            ])
            logging.info("Preprocessor for numerical and categorical data created")

            return preprocessor

        except Exception as e:
            logging.error(f"Error in creating data transformer object: {str(e)}")
            raise CustomException(e, sys.exc_info())

    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Successfully read train and test data")

            preprocessor_obj = self.get_data_transformer_object()
            logging.info("Obtained preprocessing object")

            target_column_name = "math_score"
            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]
            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info("Applying preprocessing to training and testing data")
            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]
            logging.info("Data transformation complete")

            save_object(
                file_path=self.data_transformation_config.preprocessor_ob_dir_path,
                file_name='preprocessor.pkl',
                obj=preprocessor_obj
            )
            logging.info(f"Saved the preprocessing object at {self.data_transformation_config.preprocessor_ob_dir_path}")

            return (
                train_arr, 
                test_arr, 
                os.path.join(self.data_transformation_config.preprocessor_ob_dir_path, 'preprocessor.pkl')
            )
        
        except Exception as e:
            logging.error(f"Error during data transformation: {str(e)}")
            raise CustomException(e, sys)