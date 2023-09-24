import os
import sys
from src.logger import logging
from src.exception import CustomException
from src.components.data_transformation import DataTransformation
import pandas as pd
from src.components.data_ingestion import DataIngestion

if __name__ == "__main__":
    try:
        logging.info("Training Pipeline Started")

        # Initialize the Data Ingestion Configuration  
        data_ingestion = DataIngestion()

        # Initialize the Data Ingestion
        train_data_path, test_data_path = data_ingestion.initialize_data_ingestion()

        # Initialize the Data Transformation Configuration
        data_transformation = DataTransformation()

        # Initialize the Data Transformation
        train_data, test_data, data_transformation_object = data_transformation.initialize_data_transformation(train_data_path, test_data_path)

        logging.info("Training Pipeline Completed")
        

    except Exception as e:
        logging.error("Training Pipeline Failed")
        raise CustomException("Training Pipeline Failed", e)