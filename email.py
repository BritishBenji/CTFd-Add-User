import requests as r
from config import APIKEY, BASEURL
import logging, sys, csv
import configparser


config = configparser.ConfigParser()
config.read("setup.ini")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("debug.log"), logging.StreamHandler(sys.stdout)],
    encoding="utf-8",
)

header = {"Authorization": f"Token {APIKEY}", "Content-Type": "application/json"}

payload = {
    "mail_password": config['mail']['mailPassword'],
    "mail_port": config['mail']['mailPort'],
    "mail_server": config['mail']['mailServer'],
    "mail_ssl": config["mail"].getboolean('mailSSL'),
    "mail_tls": config["mail"].getboolean('mailTLS'),
    "mail_useauth": config["mail"].getboolean('mailAUTH'),
    "mail_username": config["mail"]["mailUsername"],
    "mailfrom_addr": config["mail"]["mailFromAddress"]
}
a = r.patch(f"{BASEURL}api/v1/configs", headers=header, json=payload)

print(a.text)
