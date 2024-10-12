import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "23401377"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "a253e1cdcb1bdbad27dc4f1fcefca125")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://amangiri11:amangiri525@cluster10.s8js2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster10")
