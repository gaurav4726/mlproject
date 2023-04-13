import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split

from dataclasses import dataclass # dataclass will help to define variables


# here we are running code to check everything working thats why we import it 

from src.components.data_transformation import DataTransformation 
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv") # it will create new path artifacts/train.csv name .
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() # due to dataclass library we not defined seperately variables

    
    def initiate_data_ingestion(self):
        '''
        This function will take data from local and split train and test set data 
        '''
        logging.info("Entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\stud.csv') # Just showing basic reading of file 
            logging.info('Read the dataset as dataframe')
            # we will use exist_ok =True because if folder exist than not replace it .
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True) # create artifact folder and train data path

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)# save data 

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")
            
            return(self.ingestion_config.train_data_path,
                   self.ingestion_config.test_data_path)
        
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()  # It will create train and test data path

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
