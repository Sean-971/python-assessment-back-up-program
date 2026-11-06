import logging

# Configure logging to append to 'app.log'
logging.basicConfig(
    filename='backup.log', 
    filemode='a', # 'a' means append (this is the default)
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Write log messages
logging.info("This message is appended to the log file.")
logging.error("An error occurred during execution.")