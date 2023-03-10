import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", # this is format of error
    level=logging.INFO, # if we will enter logging.info than error message will print with above details


)

# # To check every thing is working -- in terminal enter python src/logger.py than see logs file 

# if __name__=="__main__":
#     logging.info("Start logging")

# #[ 2023-03-10 18:54:47,044 ] 21 root - INFO - Start logging  -- this format will come , 21 is line number, level name is root and message    


