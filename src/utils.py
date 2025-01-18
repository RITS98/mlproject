import os
import sys
import numpy as np
import pandas as pd
from src.exception import CustomException
from src.logger import logging
import dill

def save_object(file_path, file_name, obj):

    try:

        dir_path = os.path.join(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(os.path.join(file_path, file_name), 'wb') as file:
            dill.dump(obj, file)
    
    except Exception as e:
        raise CustomException(e, sys) 