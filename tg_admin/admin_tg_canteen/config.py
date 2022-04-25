import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("token"))
PGUSER = str(os.getenv("user"))
PGPASSWORD = str(os.getenv("password"))
DATABASE = str(os.getenv("db"))
DBHOST = str(os.getenv("ip"))

admins = [

]

ip = os.getenv("ip")

aiogram_redis = {
    'host': ip,
}

redis = {
    'address': (ip, 6379),
    'encoding': 'utf8'
}

POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASSWORD}@{DBHOST}/{DATABASE}"
