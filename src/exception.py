import sys

def error_message(error, error_detail):
    _, _, exe_tb = error_detail.exc_info()
    file_name = exe_tb.tb_frame.f_code.co_filename
    line_no = exe_tb.tb_lineno
    error_message = "Error occurred in python file: " + file_name + " at line number: " + str(line_no) + " with error message: " + str(error)

    return error_message

class CustomException(Exception):
    """Base class for exceptions in this module."""
    def __init__(self, error, error_detail):
        super().__init__(error_message(error, error_detail))
        self.error_message = error_message(error, error_detail)

    def __str__(self):
        return self.error_message
