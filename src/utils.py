import os
import sys
import pickle
import numpy as np
import pandas as pd

from src.logger import logging
from src.exception import CustomException

from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

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

def evaluate_model(X_tain, y_train, X_test, y_test, models):
    try:
        logging.info("Model Evaluation Started")
        model_report = {}
        for model_name, model in models.items():
            logging.info("Evaluating model: {}".format(model_name))
            model.fit(X_tain, y_train)
            y_pred = model.predict(X_test)
            model_report[model_name] = {
                "model": model,
                "r2_score": r2_score(y_test, y_pred),
            }
            logging.info("Model Evaluated Successfully")
        return model_report
    except Exception as e:
        logging.error("Error in evaluating model: {}".format(e))
        raise CustomException("Error in evaluating model: {}".format(e))