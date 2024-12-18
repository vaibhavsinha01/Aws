import logging

# # Create a custom logger
# logger = logging.getLogger('custom_logger')
# logger.setLevel(logging.DEBUG)

# # Create a file handler
# file_handler = logging.FileHandler('app.log', mode='w')
# file_handler.setLevel(logging.DEBUG)

# # Define formatter and add it to the handler
# formatter = logging.Formatter(
#     '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S'
# )
# file_handler.setFormatter(formatter)

# # Add handler to the custom logger
# logger.addHandler(file_handler)

# # Generate log messages
# logger.debug("This is a debug message")
# logger.info("This is an info message")
# logger.warning("This is a warning message")
# logger.error("This is an error message")
# logger.critical("This is a critical message")
logging.basicConfig(
    filename = r'C:\Users\vaibh\OneDrive\Desktop\New folder\Folder Python\Folder DataScience\Project MLOPSLearning\app.log',
    filemode = 'w',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)