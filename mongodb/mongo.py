import configparser
import pymongo

config = configparser.ConfigParser()
config.read("config.ini")

mongo = pymongo.MongoClient(
    host=config['MongoDB']['host'],
    port=int(config['MongoDB']['port']),
    username=config['MongoDB']['username'],
    password=config['MongoDB']['password'],
    serverSelectionTimeoutMS=1000
)