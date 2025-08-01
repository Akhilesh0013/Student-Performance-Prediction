import sys
# from logger import logging 


def error_message_detail(error) :

    _, _, exc_tb = sys.exc_info()

    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
            file_name, exc_tb.tb_lineno, str(error)
        )
    else:
        error_message = f"Error: {str(error)} (no traceback available)"
    return error_message



class CustomException(Exception) :
    def __init__(self,error_message):
        super().__init__(error_message)
        self.error_message= error_message_detail(error_message)
    
    def __str__(self):
        return self.error_message
    

    


    



   




