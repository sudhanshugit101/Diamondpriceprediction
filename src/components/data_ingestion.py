import os
import sys
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass

import pandas as pd
from sklearn.model_selection import train_test_split

# initialize the Data Ingestion Configuration

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "raw_data.csv")

class DataIngestion:
    def __init__(self, config=DataIngestionConfig()):
        self.ingestion_config = config

    def initialize_data_ingestion(self):
        try:
            logging.info("Data Ingestion Started")
            gem_data=pd.read_csv(os.path.join("notebook/data", 'gemstone.csv'))

            # Save the raw data
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            gem_data.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Raw Data Saved")

            # Split the data into train and test
            train_data, test_data = train_test_split(gem_data, test_size=0.2, random_state=42)
            train_data.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Train and Test Data Created")

            logging.info("Data Ingestion Completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.error("Data Ingestion Failed")
            raise CustomException("Data Ingestion Failed", e)