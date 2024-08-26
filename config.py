# bot developer @mr_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "27494535")
    API_HASH = environ.get("API_HASH", "52210cf4440a4a2b816ed1bcad615d4d")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7082109889:AAEQV69nP4zBBP9bg9nrQ7aZTxzdVK0OOtA") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5601277336').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 

    PICS = (environ.get('PICS', ''))
    
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://raja:raja@cluster0.uwezr4a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002175614080'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "MoviesUpdate_07") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
