import logging
from logging.handlers import RotatingFileHandler
import os
import sys
import coloredlogs

def setup_logger():
    
    coloredlogs.install(level='INFO', fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s', stream=sys.stdout, level_styles={
        'info': {'color': 'green'},
        'warning': {'color': 'yellow'},
        'error': {'color': 'red', 'bold': True},
        'critical': {'color': 'red', 'bold': True}
    })
    

    log_level = os.environ.get("LOG_LEVEL", "INFO")
    
    os.makedirs("backend/logs", exist_ok=True)

    file_handler = RotatingFileHandler(
        "backend/logs/app.log", 
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(log_level)

    logging.getLogger().addHandler(file_handler)
    logging.getLogger().setLevel(log_level)
    
    logging.getLogger("httpx").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)
    logging.getLogger("primp").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)