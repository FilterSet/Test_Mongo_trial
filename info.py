# Don't Remove Credit @T4TVSeries1
# Subscribe YouTube Channel For Amazing Bot @T4TVSeries1
# Ask Doubt on telegram https://t.me/T4TVSeries1

import re
from os import environ
from dotenv import load_dotenv
from Script import script

load_dotenv()

# Helper to convert env string to boolean
def str_to_bool(value):
    return str(value).lower() == "true"

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', '')
API_ID = int(environ.get('API_ID', 0))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

# This Pictures Is For Start Message Picture, You Can Add Multiple By Giving One Space Between Each.
PICS = (environ.get('PICS', '')).split()

# Admins & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else ADMINS

# This Channel Is For When User Start Your Bot Then Bot Send That User Name And Id In This Log Channel, Same For Group Also.
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0))

# This Is File Channel Where You Upload Your File Then Bot Automatically Save It In Database
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '').split()]

# auth_channel means force subscribe channel.
REQUEST_TO_JOIN_MODE = str_to_bool(environ.get('REQUEST_TO_JOIN_MODE', ''))
TRY_AGAIN_BTN = str_to_bool(environ.get('TRY_AGAIN_BTN', ''))

auth_channel = environ.get('AUTH_CHANNEL', '')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None

reqst_channel = environ.get('REQST_CHANNEL', '')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None

INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))

support_chat_id = environ.get('SUPPORT_CHAT_ID', '')
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None

FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]

DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '').split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', '')
DATABASE_NAME = environ.get('DATABASE_NAME', '')
COLLECTION_NAME = environ.get('COLLECTION_NAME', '')

MULTIPLE_DATABASE = str_to_bool(environ.get('MULTIPLE_DATABASE', ''))

O_DB_URI = environ.get('O_DB_URI', '')
F_DB_URI = environ.get('F_DB_URI', '')
S_DB_URI = environ.get('S_DB_URI', '')

# Premium & Referral Settings
PREMIUM_AND_REFERAL_MODE = str_to_bool(environ.get('PREMIUM_AND_REFERAL_MODE', ''))
REFERAL_COUNT = int(environ.get('REFERAL_COUNT', '0'))
REFERAL_PREMEIUM_TIME = environ.get('REFERAL_PREMEIUM_TIME', '')
PAYMENT_QR = environ.get('PAYMENT_QR', '')
PAYMENT_TEXT = environ.get('PAYMENT_TEXT', '')

# Clone Mode
CLONE_MODE = str_to_bool(environ.get('CLONE_MODE', ''))
CLONE_DATABASE_URI = environ.get('CLONE_DATABASE_URI', '')
PUBLIC_FILE_CHANNEL = environ.get('PUBLIC_FILE_CHANNEL', '')

# Links
GRP_LNK = environ.get('GRP_LNK', '')
CHNL_LNK = environ.get('CHNL_LNK', '')
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', '')
OWNER_LNK = environ.get('OWNER_LNK', '')

# Feature Toggles
AI_SPELL_CHECK = str_to_bool(environ.get('AI_SPELL_CHECK', ''))
PM_SEARCH = str_to_bool(environ.get('PM_SEARCH', ''))
BUTTON_MODE = str_to_bool(environ.get('BUTTON_MODE', ''))
MAX_BTN = str_to_bool(environ.get('MAX_BTN', ''))
IS_TUTORIAL = str_to_bool(environ.get('IS_TUTORIAL', ''))
IMDB = str_to_bool(environ.get('IMDB', ''))
AUTO_FFILTER = str_to_bool(environ.get('AUTO_FFILTER', ''))
AUTO_DELETE = str_to_bool(environ.get('AUTO_DELETE', ''))
LONG_IMDB_DESCRIPTION = str_to_bool(environ.get("LONG_IMDB_DESCRIPTION", ''))
SPELL_CHECK_REPLY = str_to_bool(environ.get("SPELL_CHECK_REPLY", ''))
MELCOW_NEW_USERS = str_to_bool(environ.get('MELCOW_NEW_USERS', ''))
PROTECT_CONTENT = str_to_bool(environ.get('PROTECT_CONTENT', ''))
PUBLIC_FILE_STORE = str_to_bool(environ.get('PUBLIC_FILE_STORE', ''))
NO_RESULTS_MSG = str_to_bool(environ.get("NO_RESULTS_MSG", ''))
USE_CAPTION_FILTER = str_to_bool(environ.get('USE_CAPTION_FILTER', ''))

# Verification
VERIFY = str_to_bool(environ.get('VERIFY', ''))
VERIFY_SHORTLINK_URL = environ.get('VERIFY_SHORTLINK_URL', '')
VERIFY_SHORTLINK_API = environ.get('VERIFY_SHORTLINK_API', '')
VERIFY_TUTORIAL = environ.get('VERIFY_TUTORIAL', '')

VERIFY_SECOND_SHORTNER = str_to_bool(environ.get('VERIFY_SECOND_SHORTNER', ''))
VERIFY_SND_SHORTLINK_URL = environ.get('VERIFY_SND_SHORTLINK_URL', '')
VERIFY_SND_SHORTLINK_API = environ.get('VERIFY_SND_SHORTLINK_API', '')

# Shortlink
SHORTLINK_MODE = str_to_bool(environ.get('SHORTLINK_MODE', ''))
SHORTLINK_URL = environ.get('SHORTLINK_URL', '')
SHORTLINK_API = environ.get('SHORTLINK_API', '')
TUTORIAL = environ.get('TUTORIAL', '')

# Misc
CACHE_TIME = int(environ.get('CACHE_TIME', 1800))
MAX_B_TN = environ.get("MAX_B_TN", "5")
PORT = environ.get("PORT", "8080")
MSG_ALRT = environ.get('MSG_ALRT', '')
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)

# Choose Options
LANGUAGES = ["malayalam", "mal", "tamil", "tam", "english", "eng", "hindi", "hin", "telugu", "tel", "kannada", "kan"]
SEASONS = [f"season {i}" for i in range(1, 11)]
EPISODES = [f"E{str(i).zfill(2)}" for i in range(1, 41)]
QUALITIES = ["360p", "480p", "720p", "1080p", "1440p", "2160p"]
YEARS = [str(y) for y in range(1900, 2026)]

# Streaming
STREAM_MODE = str_to_bool(environ.get('STREAM_MODE', ''))
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))
ON_HEROKU = 'DYNO' in environ
URL = environ.get("URL", "")

# Rename
RENAME_MODE = str_to_bool(environ.get('RENAME_MODE', ''))

# Auto Approve
AUTO_APPROVE_MODE = str_to_bool(environ.get('AUTO_APPROVE_MODE', ''))

# Reactions
REACTIONS = ["🤝", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"]

# Final DB assignments
if not MULTIPLE_DATABASE:
    USER_DB_URI = DATABASE_URI
    OTHER_DB_URI = DATABASE_URI
    FILE_DB_URI = DATABASE_URI
    SEC_FILE_DB_URI = DATABASE_URI
else:
    USER_DB_URI = DATABASE_URI
    OTHER_DB_URI = O_DB_URI
    FILE_DB_URI = F_DB_URI
    SEC_FILE_DB_URI = S_DB_URI
    #
