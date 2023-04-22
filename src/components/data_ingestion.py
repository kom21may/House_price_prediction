import os
#os used becz to create file path and join file path
import sys #system error used in exception

from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass
import pandas as pd
from sklearn.model_selection import train_test_split

from src.components.data_transformation import DataTransformation
'''
An artifact is a machine learning term that is used to describe the output created by the training process. Output could be a fully trained model, a model checkpoint, or a file created during the training process.
'''
#Initialize the data Ingestion Configuration
@dataclass
class DataIngestionConfig:
    path=os.getcwd()
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')
    
#create a class for data ingestion
class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    def initiate_data_ingestion(self):
        logging.info("Data Ingestion Starts")
        try:
            df=pd.read_csv(os.path.join('E:\kdrama\ineuron\ineuron\gems_price_prediction_pipeline\notebooks\data\gemstone.csv'))
            logging.info("Dataset read as pandas Dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info('Train_test_split started')
            train_set,test_set=train_test_split(df,test_size=0.3,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info('Ingestion of Data is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

            
            
        except Exception as e:
            logging.info("Exception occured in data Ingestion step")
            raise CustomException(e,sys)
            