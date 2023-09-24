import os
import sys
import pickle
import numpy as np
import pandas as pd

from src.logger import logging
from src.exception import CustomException

def save_object(obj, file_path):
    try:
        logging.info("Saving object to file path: {}".format(file_path))
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as f:
            pickle.dump(obj, f)
        logging.info("Object saved successfully")
    except Exception as e:
        logging.error("Error in saving object: {}".format(e))
        raise CustomException("Error in saving object: {}".format(e))

        