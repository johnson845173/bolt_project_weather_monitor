username = "vjnzvebppbpdhu"
# PostgreSQL password
password = "9d68913688fd60c9b45c2ac527656d277b7d05152b265ffa5883d62e54fe695e"
# PostgreSQL host address
host = "ec2-44-209-158-64.compute-1.amazonaws.com"
# PostgreSQL port
port = "5432"
# PostgreSQL DB
db = "detqb1eealmc9h"

url = f"postgres://{username}:{password}@{host}/{db}"

bolt_name = "BOLT14854650"

bolt_api = "487b1d2a-e884-4e88-b88c-526aa4bc7721"

geturl = f"https://cloud.boltiot.com/remote/{bolt_api}/serialRead?till=20&deviceName={bolt_name}"

request_url = f"https://cloud.boltiot.com/remote/{bolt_api}/serialWrite?data=RD&deviceName={bolt_name}"

telegram_chat_id = "@tempratureee"

telegram_bot_id = "bot5326832976:AAGBiKuCwYo2_9oMF6-50_WKlhDD_nIoI2A"

