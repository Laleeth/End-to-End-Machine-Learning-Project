
import sys
import logging



# define Python user-defined exceptions
def error_text(error,error_detail:sys):
    _,_,_exc_tb=error_detail.exc_info()
    file_name=_exc_tb.tb_frame.f_code.co_filename
    error_message="Something is wrong please check the script [{0}] line number [{1}] error message [{2}]".format(
    file_name,_exc_tb.tb_lineno,str(error))
    return error_message
    
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_text(error_message,error_detail=error_detail)

    def __str__(self):
        return self.error_message
 

        

if __name__=="__main__":


    try:
        a=10/0
    except Exception as e:
        logging.info("Error Occured at division")
        raise CustomException(e,sys)