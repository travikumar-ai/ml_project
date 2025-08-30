import sys


def error_msg_details(error, error_details: sys):

    _, _, exc_tb = error_details.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename
    error_msg = f"Error occurred in python script name [{file_name}] \
        line number [{exc_tb.tb_lineno}] error message [{error}]"

    return error_msg


class CustomException(Exception):
    def __init__(self, error, error_details: sys):
        super().__init__(error)
        self.error_message = error_msg_details(error, error_details)

    def __str__(self):
        return self.error_message
