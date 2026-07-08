import logging

from config import LOG_FILE

# Create logger
logger = logging.getLogger("bronze_logger") #created a logger with bronze_logger as its name
logger.setLevel(logging.INFO) #Normal messages Reading files. Saving files. Finished successfully.

# Avoid adding duplicate handlers if imported multiple times
if not logger.handlers:

    # Write logs to a file. handler means Where should the logger send messages   handler opens the file. If the file doesn't exist... Python automatically creates it.
    file_handler = logging.FileHandler(LOG_FILE)
    #Formatter controls how logs look.
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
        #2026-07-03 18:25:44    INFO    Reading Paris
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    #when logger recieves a message (logger.info()) he sends it to the handler he has 