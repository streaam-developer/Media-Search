import re
import os
import time
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '904789'))
API_HASH = environ.get('API_HASH', '2262ef67ced426b9eea57867b11666a1')
BOT_TOKEN = environ.get('BOT_TOKEN', "5120091936:AAGX5L29-BRpyA_mv7j-A60h_e8jvZF0JgM")
BOT_USERNAME = environ.get('BOT_USERNAME', 'ipapcornbot')


# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '622730585 1003337276 5414689790 5059740089 5739623984 6924888856').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]



# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://cinihe6110:n9md7VCwteiuzgC8@cluster0.d8aqy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")   # IF Multiple Database Is False Then Fill Only This Database Url.
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'sampless')
SAVE_USER = os.environ.get("SAVE_USER", "no").lower()
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")
DATABASE_NAME_2 = str(os.environ.get("DATABASE_NAME_2", "Cluster0"))
AUTH_USERS_2 = set(str(x) for x in os.environ.get("AUTH_USERS_2", "").split())
DATABASE_URI_2 = os.environ.get("DATABASE_URI_2", "mongodb+srv://cinihe6110:n9md7VCwteiuzgC8@cluster0.d8aqy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")


# Manual Filter Commands 😁
ADD_FILTER_CMD = os.environ.get("ADD_FILTER_CMD", "add")
DELETE_FILTER_CMD = os.environ.get("DELETE_FILTER_CMDD", "del")
DELETE_ALL_CMD = os.environ.get("DELETE_ALL_CMDD", "delall")
CONNECT_COMMAND = os.environ.get("CONNECT_COMMANDD", "connect")
DISCONNECT_COMMAND = os.environ.get("DISCONNECT_COMMANDD", "disconnect")


# Messages
default_start_msg = """
**Hi {}, I'm Media Search Bot or ypu can call me as Auto-Filter Bot**
Here you can search files in Inline mode as well as PM, Use the below buttons to search files or send me the name of file to search.
"""
START_MSG = environ.get('START_MSG', default_start_msg)

FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "")
OMDB_API_KEY = environ.get("OMDB_API_KEY", "")
if FILE_CAPTION.strip() == "":
    CUSTOM_FILE_CAPTION=None
else:
    CUSTOM_FILE_CAPTION=FILE_CAPTION
if OMDB_API_KEY.strip() == "":
    API_KEY=None
else:
    API_KEY=OMDB_API_KEY

BOT_START_TIME = time.time()
