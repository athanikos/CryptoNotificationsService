from datetime import datetime
from flask import jsonify
from cryptodataaccess.RatesRepository import RatesRepository
#from cryptodataaccess.TransactionRepository import TransactionRepository
import jsonpickle
from CryptoNotificationsService.helpers import log_error
from kafkaHelper.kafkaHelper import consume, produce
import notifiers

DEFAULT_CURRENCY = "EUR"
DATE_FORMAT = "%Y-%m-%d"


class NotificationService:


    def __init__(self, config):
       self.rates_repo = RatesRepository(config, log_error)
       # self.trans_repo = TransactionRepository(config, log_error)

    def notify(self):
        telegram = notifiers.get_notifier('telegram')
        print(telegram.required)
        telegram.notify(message='hi', chat_id='dachatid', token='datoken')

        # telegram.notify(message='hello CHRIS!',chat_id='1222543667', token='1267429467:AAHg2e1RoZplE67O_9uVCDOB2ctT5Bf6Z9o')
        # telegram.notify(message='hello CHRIS!',chat_id='1213236780', token='1267429467:AAHg2e1RoZplE67O_9uVCDOB2ctT5Bf6Z9o')

        # notifications = requests.get('http://localhost:5000/api/v1/user-channels/1/telegram')
        # json_data = json.loads(notifications.json())
        # print ( type(json_data))
        # print(json_data)
        # print (json_data[0]['chat_id'])

        # telegram.notify(message='hi from py', chat_id=json_data[0]['chat_id'], token=get_password('CryptoNotifier', 'token') )