import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging


@dataclass
class DataIngestionConfig:
    # Paths for storing training, testing, and raw data
    train_data_path: str = os.path.join('artifacts', 'train_csv')
    test_data_path: str = os.path.join('artifacts', 'test_csv')
    raw_data_path: str = os.path.join('artifacts', 'raw_data_csv')


class DataIngestion:
    def __init__(self):
        """
        Initialize DataIngestion with the default configuration, as soon as object is created for this class, this will initialize the paths 
        """
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        """
        Handles the process of data ingestion: reading data, splitting into
        training and testing sets, and saving these datasets.
        """
        logging.info("Entered into data ingestion method.")
        
        try:
            # Load the dataset from an Excel file
            # we can also load data from dbs, api, cloud etc
            df = pd.read_excel(r"H:\CampusX_DS\week43 - My Projects Aug 2024\mlops_laptop_price_prediction\notebook\smartprix_laptop_cleaned_v8.xlsx")
            logging.info("Read dataset which was already cleaned as DataFrame.")
            
            # Ensure the directory for raw data exists
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)
            
            # Save the raw dataset to CSV
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Raw data saved.")
            
            # Split the dataset into training and testing sets
            logging.info("Train-test split initiated.")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            
            # Save the training and testing datasets to CSV
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            
            logging.info("Data ingestion completed.")
            
            # Return the paths of training and testing data to be used in the next step which is data_transformation
            return (self.ingestion_config.train_data_path, self.ingestion_config.test_data_path)
        
        except Exception as e:
            # Raise a custom exception if an error occurs
            raise CustomException(e, sys)
        
        
        
# if __name__ == "__main__":
#     obj = DataIngestion()                   #this will initialize the path of train, test & raw
#     obj.initiate_data_ingestion()           #this will create artifacts folder & update the logs