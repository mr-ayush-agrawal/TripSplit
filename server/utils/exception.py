import sys
from server.utils.logger import logging

class CustomError(Exception):
    def __init__(self, err_msg, err_details : sys = sys):
        self.error_message = err_msg
        _, _, exc_tb = err_details.exc_info()

        self.line_number = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename
 
    def __str__(self):
        return f"Error Occured in Python Script [{self.file_name}]\nline number[{self.line_number}]\nError Message : [{str(self.error_message)}]"
    