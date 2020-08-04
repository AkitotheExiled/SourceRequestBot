from configparser import ConfigParser
from src.database.database import Database
from src.classes.logger import Logger
import os

temp_path = os.path.dirname(os.path.abspath(__file__))
config = os.path.join(temp_path, "../../config.ini")
print(config)

class RedditBaseClass:
    def __init__(self):
        try:
            self.CONFIG = ConfigParser()
            self.CONFIG.read(config)
        # Retrieving User information from config.ini for PRAW
            self.user = self.CONFIG.get('main', 'USER')
            self.password = self.CONFIG.get('main', 'PASSWORD')
            self.client = self.CONFIG.get('main', 'CLIENT_ID')
            self.secret = self.CONFIG.get('main', 'SECRET')
            self.delay = self.CONFIG.getint('main', 'DELAY')
            self.subreddit = self.CONFIG.get('main', 'SUBREDDIT')
            self.flair = self.CONFIG.get('main', 'FLAIR')
            self.wait_timer = self.CONFIG.getint('main', 'RECHECK_WAIT')
            self.removal_note = self.CONFIG.get('main', 'REMOVAL_REASON')
            self.log = Logger()
            self.logger = self.log.logger
        except Exception:
            self.logger.info(f"ERROR RETRIEVING CONFIG: {config}", exc_info=True)

