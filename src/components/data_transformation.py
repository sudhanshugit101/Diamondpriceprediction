import os
import sys
import numpy as np
import pandas as pd
from src.logger import logging
from src.exception import CustomException
from src.utils import save_object
from dataclasses import dataclass

from sklearn.impute import SimpleImputer 
from sklearn.preprocessing import StandardScaler 
from sklearn.preprocessing import OrdinalEncoder 

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

@dataclass

class DataTransformationConfig:
    preprocessor_object_file_path=os.path.join("artifacts","preprocessor_object.pkl")

class DataTransformation:
    def __init__(self):
        self.config = DataTransformationConfig()

    def get_data_transformation_object(self):
        try:
            logging.info("Initiating data transformation")

            # Segregating numerical and categorical variables
            categorical_variables =  ['cut', 'color', 'clarity']
            numerical_variables = ['carat', 'depth', 'table', 'x', 'y', 'z']

            cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']

            # Creating pipeline for numerical variables
            logging.info("Creating pipeline for numerical variables")
            num_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='median')),
                ('scaler',StandardScaler())

                ]
            )

            # Creating pipeline for categorical variables
            logging.info("Creating pipeline for categorical variables")
            cat_pipeline=Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('ordinalencoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                ('scaler',StandardScaler())
                ]
            )

            # Creating column transformer
            logging.info("Creating column transformer")
            preprocessor=ColumnTransformer([
            ('num_pipeline',num_pipeline,numerical_variables),
            ('cat_pipeline',cat_pipeline,categorical_variables)
            ]
            )

            return preprocessor
        except Exception as e:
            logging.error("Exception occured while initiating data transformation")
            raise CustomException(e)

    def initialize_data_transformation(self, train_data_path, test_data_path):
        try:
            
            logging.info("Reading train and test data")
            train_df = pd.read_csv(train_data_path)
            test_df = pd.read_csv(test_data_path)

            logging.info('Read train and test data completed')
            logging.info(f'Train Dataframe Head : \n{train_df.head().to_string()}')
            logging.info(f'Test Dataframe Head  : \n{test_df.head().to_string()}')

            logging.info("Obtaining preprocessor object")
            preprocessor = self.get_data_transformation_object()

            target = 'price'
            drop_cols = [target, 'id']

            input_train = train_df.drop(drop_cols, axis=1)
            input_test = test_df.drop(drop_cols, axis=1)
            target_train = train_df[target]
            target_test = test_df[target]

            logging.info("Fitting the preprocessor object")
            input_train_transformed = preprocessor.fit_transform(input_train)
            input_test_transformed = preprocessor.transform(input_test)

            train_data=np.concatenate((input_train_transformed,target_train.values.reshape(-1,1)),axis=1)
            test_data=np.concatenate((input_test_transformed,target_test.values.reshape(-1,1)),axis=1)

            logging.info("Saving the preprocessor object")
            save_object(preprocessor, self.config.preprocessor_object_file_path)

            return train_data, test_data, self.config.preprocessor_object_file_path


        except Exception as e:
            logging.error("Exception occured while initiating data transformation")
            raise CustomException(e)