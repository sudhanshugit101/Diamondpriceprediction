import sys

def error_message_detail(error):
    _, _, exe_tb = sys.exc_info()
    file_name = exe_tb.tb_frame.f_code.co_filename
    line_number = exe_tb.tb_lineno
    error_message = "Error occurred in python file: [{0}] at line number: [{1}] with error message: [{2}] ".format(file_name, line_number, str(error))
    return error_message

class CustomException(Exception):
    """Base class for exceptions in this module."""
    def __init__(self, error):
        super().__init__(error_message_detail(error))
        self.error_message = error_message_detail(error)

    def __str__(self):
        return self.error_message
