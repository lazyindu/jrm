import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "12936189")

API_HASH = os.environ.get("API_HASH", "7e24008e8ec33a397155b6a9d618497b")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6396913711:AAFJpA3eMFa1Nzo9aHVGsuPys-mSocXemUY") 

FORCE_SUB = os.environ.get("FORCE_SUB", "-1001492950585") 

DB_NAME = os.environ.get("DB_NAME","Cluster0Rename")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://gill1322:gill1322@cluster0rename.x8jiptm.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1166670205').split()]

# Bot_Username = "@LazyPrincessXBOT"
BOT_USERNAME = os.environ.get("BOT_USERNAME", "@FileRenamesRobot")
MAX_ACTIVE_TASKS = int(os.environ.get("MAX_ACTIVE_TASKS", "5"))
MAX_FORWARD = int(os.environ.get("MAX_FORWARD", "20"))

PORT = os.environ.get('PORT', '8080')

Lazy_session = {}
Lazy_api_id ={}
Lazy_api_hash ={}

String_Session  = "None"

Permanent_4gb = "-100XXX"
