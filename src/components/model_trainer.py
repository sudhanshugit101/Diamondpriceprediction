import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_model
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.neighbors import KNeighborsRegressor

@dataclass

class ModelTrainerConfig:
    trained_model_path=os.path.join("actifacts", 'model.pkl')

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
                "LinearRegression": LinearRegression(),
                "Ridge": Ridge(),
                "Lasso": Lasso(),
                "ElasticNet": ElasticNet(),
                "RandomForestRegressor": RandomForestRegressor(),
                "GradientBoostingRegressor": GradientBoostingRegressor(),
                "KNeighborsRegressor": KNeighborsRegressor()
            }

            params={
                "LinearRegression":{},
                "Ridge": {},
                "Lasso": {},
                "ElasticNet": {},
                "RandomForestRegressor":{
                    # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                    # 'max_features':['sqrt','log2',None],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "GradientBoostingRegressor":{
                    # 'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
                    'learning_rate':[.1,.01,.05,.001],
                    'subsample':[0.6,0.7,0.75,0.8,0.85,0.9],
                    # 'criterion':['squared_error', 'friedman_mse'],
                    # 'max_features':['auto','sqrt','log2'],
                    'n_estimators': [8,16,32,64,128,256]
                },
                "KNeighborsRegressor":{
                    'n_neighbors':[2,3,4,5,6,7,8,9,10],
                    'weights':['uniform','distance'],
                    'algorithm':['auto','ball_tree','kd_tree','brute']
                }
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