import requests as r
from config import APIKEY, BASEURL
import logging, sys, csv

logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler(sys.stdout)
    ],
    encoding="utf-8"
)

header = {"Authorization": f"Token {APIKEY}", "Content-Type": "application/json"}

with open("./users.csv", "r") as file:
    datareader = csv.reader(file)
    for row in datareader:
        payload = {"name":row[0], "email":row[1], "password":row[2]}
        a = r.post(BASEURL+"/api/v1/users",headers=header, json=payload)
        if a.status_code == 400:
            if list(a.json()['errors'].keys())[0] =="email":
                logging.critical(f"Server returned 400: {a.json()['errors']['email'][0]}")
            else:
                logging.warning(f"Server returned 400: {a.json()['errors']}")
        if a.status_code == 200:
            logging.info("Server returned code 200, Success")
            with open("success.txt", "a") as writeFile:
                writeFile.write(row[0]+'\t'+row[1]+'\n')
        else:
            logging.info(a.content)
