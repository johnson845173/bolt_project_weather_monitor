username = "Your heroku usernme" 
# PostgreSQL password
password = "Your Heroku Password"
# PostgreSQL host address
host = "Your Data Base Password"
# PostgreSQL port
port = "port number"
# PostgreSQL DB
db = "database name"

url = f"postgres://{username}:{password}@{host}/{db}"

bolt_name = "Bolt device name"

bolt_api = "Secret IP adress"

geturl = f"https://cloud.boltiot.com/remote/{bolt_api}/serialRead?till=20&deviceName={bolt_name}"

request_url = f"https://cloud.boltiot.com/remote/{bolt_api}/serialWrite?data=RD&deviceName={bolt_name}"

telegram_chat_id = "@Telegram chat id"

telegram_bot_id = "telegram bot id"

