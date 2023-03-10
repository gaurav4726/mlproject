import sys # sys info  have all details of exceptions 
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb=error_detail.exc_info() # error_detail have all info of error which can get from exc_tb which is 3rd parameter. Rest 2 not rquired due to which _,_ used
    file_name=exc_tb.tb_frame.f_code.co_filename # exc_tb will give the file name
    error_message="Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error)) # format of exceptions

    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message

#Error will raise and than we can save it to logs. To save it need to call logging file "from src.logger import logging"
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e: 
        logging.info("It can not divide by 0") 
        raise CustomException(e,sys)   

    