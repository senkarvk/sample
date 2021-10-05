import logging
from pathlib import Path
logFolder=Path("./logs")
log_file=logFolder/"test_summary.log"

class LogHandle:
    @staticmethod
    def createLogger():
        logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)
        logger=logging.getLogger()
        return logger