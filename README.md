## End to End Machine Learning Project

#### Directory Structure

Directory structure:  
.
├── README.md  
├── app.py  
├── artifacts  
│   ├── data.csv  
│   ├── models  
│   │   └── model.pkl  
│   ├── preprocessor  
│   │   └── preprocessor.pkl  
│   ├── test.csv  
│   └── train.csv  
├── mlproject.egg-info  
│   ├── PKG-INFO  
│   ├── SOURCES.txt  
│   ├── dependency_links.txt  
│   ├── requires.txt  
│   └── top_level.txt  
├── notebook  
│   ├── EDA Student Performance.ipynb  
│   ├── Model Training.ipynb  
│   └── data  
│       └── stud.csv  
├── requirements.txt  
├── setup.py  
├── src   
│   ├── __init__.py  
│   ├── __pycache__  
│   │   ├── __init__.cpython-312.pyc  
│   │   ├── exception.cpython-312.pyc  
│   │   ├── logger.cpython-312.pyc  
│   │   └── utils.cpython-312.pyc  
│   ├── components  
│   │   ├── __init__.py  
│   │   ├── __pycache__  
│   │   │   ├── __init__.cpython-312.pyc  
│   │   │   ├── data_transformation.cpython-312.pyc  
│   │   │   └── model_trainer.cpython-312.pyc  
│   │   ├── data_ingestion.py  
│   │   ├── data_transformation.py  
│   │   └── model_trainer.py  
│   ├── exception.py  
│   ├── logger.py  
│   ├── pipeline  
│   │   ├── __init__.py  
│   │   ├── __pycache__  
│   │   │   ├── __init__.cpython-312.pyc  
│   │   │   └── predict_pipeline.cpython-312.pyc  
│   │   ├── predict_pipeline.py  
│   │   └── train_pipeline.py  
│   └── utils.py  
└── templates  
    ├── home.html  
    └── index.html  


This project is about predicting the math score of a student when different parameters are given.

The parameters are as follows ->
- gender : sex of students  -> (Male/female)
- race/ethnicity : ethnicity of students -> (Group A, B,C, D,E)
- parental level of education : parents' final education ->(bachelor's degree,some college,master's degree,associate's degree,high school)
- lunch : having lunch before test (standard or free/reduced) 
- test preparation course : complete or not complete before test
- math score
- reading score
- writing score

In this machine learning project, various models are used like ->

- Linear Regression
- Decision Tree
- Random Forest
- Gradient Boosting
- Ada Boosting
- XGBoosting

The Grid Search method is employed for hyperparameter tunning. 

All important advanced methods like Pipeline, Column Transformer, Standard Scaler, One Hot Encoding and many more are used for preprocessing of the data.

A small flask applicatioon is also present to create a simple web page which is used for prediction.