"""
Logger is the global logging function for ProdFloorTool.py
"""
import logging
import socket

def setup_logger(name):
    """
    The setup_logger function is the main logging function for logger.py
    """
    #Get PC host name
    hostname = socket.gethostname()

    #Log variables
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(name)

    #Create a file handler
    handler = logging.FileHandler('\\\\fs01\\share\\IT\\Shane\\log\\ProdFloorTool.log')
    handler.setLevel(logging.INFO)

    #Create a logging format
    formatter = logging.Formatter(hostname + ' - %(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    #Add the handlers to the logger
    logger.addHandler(handler)

    return logger
