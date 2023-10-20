import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_model
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

@dataclass

class ModelTrainerConfig:
    trained_model_path=os.path.join("artifacts", 'model.pkl')

class ModelTrainer:
    def __init__(self):
        self.config = ModelTrainerConfig()

    def initialize_model_training(self, train_data, test_data):
        try:
            
            logging.info("Data Splitting Started")
            # Split the data into X and y
            X_train, y_train, X_test, y_test = (
                train_data[:,:-1],
                train_data[:,-1],
                test_data[:,:-1],
                test_data[:,-1]
            )

            models = {
                "GradientBoostingRegressor": GradientBoostingRegressor()
            }
            
            params={
                "GradientBoostingRegressor":{}
            }
            model_report: dict=evaluate_model(X_train, y_train=y_train, X_test=X_test, y_test=y_test, models=models, params=params)

            best_model_name = max(model_report, key=lambda x: model_report[x]['r2_score'])

            best_model_score = model_report[best_model_name]['r2_score']

            if best_model_score < 0.6:
                raise CustomException("Best model score is less than 0.6")
            
            save_object(
                file_path=self.config.trained_model_path,
                obj=model_report[best_model_name]['model']
            )

            logging.info("Model Training Completed Successfully")
            
            r2_score = model_report[best_model_name]['r2_score']
            return r2_score
        
        except Exception as e:
            logging.error("Model Training Failed")
            raise CustomException("Model Training Failed")