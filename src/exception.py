import logging
import sys
from src.logger import logging  # Import to run the configuration


def error_msg_details(error: Exception) -> str:
    """
    Formats a detailed error message including file name and line number.
    Must be called from within an 'except' block.
    """
    # sys.exc_info() gets details about the exception currently being handled
    _, _, exc_tb = sys.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename
    # Using parentheses for multi-line f-strings is a bit cleaner
    error_msg = (f"Error occurred in python script name [{file_name}] "
                 f"line number [{exc_tb.tb_lineno}] error message [{str(error)}]")

    return error_msg


class CustomException(Exception):
    def __init__(self, error: Exception):
        # Generate the detailed error message and pass it to the parent class.
        # This makes a custom __str__ method redundant.
        self.error_message = error_msg_details(error)
        super().__init__(self.error_message)

if __name__ == "__main__":
    logging.info("Starting a test run that will handle an exception.")
    
    try:
        # This will cause a ZeroDivisionError
        a = 1/0
    except Exception as e:
        # The error is caught. We log it but DO NOT raise it again.
        # This allows the program to continue.
        logging.error("A non-critical error was caught and handled.")
        custom_ex = CustomException(e)
        logging.error(f"Error details: {custom_ex.error_message}")
        print(custom_ex.error_message)
        # print("\nAn error occurred, but we handled it. Check the logs. The program will not stop.")

    # Because the exception was handled and not raised, execution continues to this point.
    # print("\nProgram finished successfully after handling the error.")
    logging.info("Test run finished.")