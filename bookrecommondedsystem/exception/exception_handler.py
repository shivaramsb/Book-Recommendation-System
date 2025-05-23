import os
import sys

class AppException(Exception):
    """
    Organization: Durgesh Singh
    AppException is customized exception class designed to capture refined details about Exception
    such as python script file line number along with error message
    with custom exception one can easily spot source of error and provide quick fix.

    """
def __init__(self, error_message: Exception, error_detail: sys):
    """
    Param error_message : error message in string format

    """

    super().__init__(error_message)
    self.error_message = AppException.error_message_detail(error_message, error_detail=error_detail)

@staticmethod
def error_message_detail(error:Exception, error_detail: sys):
    """
    error: Exception object raise from module
    error_detail: is sys module contains detail information about system execution imformation.

    """
    _, _, exc_tb = error_detail.exc_info()
    #extracting file name from exception trackback
    file_name = exc_tb.tb_frame.f_code.co_filename

    # preparing error message
    error_message = f"Error occured python script name [{file_name}]" \
                    f"Line number [{exc_tb.tb_lineno}] error message [{error}]."
    
    return error_message

def __repr__(self):
    """
    Formating object of Application
    
    """
    return AppException.__name__.__str__()

def __str__(self):
    """
    Formating how a object should be visible if used in print statement.

    """
    return self.error_message()