import os
from keyring import get_password
from werkzeug.utils import import_string

DB = "notifications_service"
PORT = 27017
MONGO_IP = "127.0.0.1"
KAFKA_BROKERS = "127.0.0.1:9092"
BALANCES_TOPIC_NAME = "balances"


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SERVERNAME = "localhost"
    PORT = PORT
    DATABASE = DB
    USERNAME = ""
    PASSWORD = ""
    LOGS_PATH = '../CryptoNotificationsService/logs/CryptoNotificationsService.log'
    KAFKA_BROKERS = KAFKA_BROKERS
    BALANCES_TOPIC_NAME = BALANCES_TOPIC_NAME


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SERVERNAME = "127.0.0.1"
    PORT = PORT
    DATABASE = DB
    USERNAME = "admin"
    PASSWORD = "admin"
    LOGS_PATH = '../CryptoNotificationsService/logs/CryptoNotificationsService.log'
    KAFKA_BROKERS = KAFKA_BROKERS
    BALANCES_TOPIC_NAME = BALANCES_TOPIC_NAME


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    SERVERNAME = MONGO_IP
    PORT = PORT
    DATABASE = DB
    USERNAME = ""
    PASSWORD = ""
    LOGS_PATH = '../CryptoNotificationsService/logs/CryptoNotificationsService.log'
    KAFKA_BROKERS = KAFKA_BROKERS
    BALANCES_TOPIC_NAME = BALANCES_TOPIC_NAME


config = {
    "development": "CryptoNotificationsService.config.DevelopmentConfig",
    "production": "CryptoNotificationsService.config.ProductionConfig",
    "default": "CryptoNotificationsService.config.DevelopmentConfig",
}


def configure_app():
    config_name = os.getenv('FLASK_ENV', 'CryptoNotificationsService.config.DevelopmentConfig')
    cfg = import_string(config_name)()
    cfg.USERNAME = get_password('CryptoNotificationsService', 'USERNAME')
    cfg.PASSWORD = get_password('CryptoNotificationsService', cfg.USERNAME)
    return cfg
