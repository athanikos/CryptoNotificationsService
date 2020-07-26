import pymongo
from flask import Flask, jsonify, request
from flask.blueprints import Blueprint
from CryptoNotificationsService.NotificationService import NotificationService
from CryptoNotificationsService.config import configure_app
import atexit


bp = Blueprint(__name__.split('.')[0], __name__.split('.')[0])
#cs = NotificationService(configure_app())

def create_app():
    the_app = Flask(__name__.split('.')[0], instance_relative_config=True)
    the_app.register_blueprint(bp)
    #start(cs)
    return the_app


@bp.app_errorhandler(pymongo.errors.ServerSelectionTimeoutError)
def handle_error(error):
    message = [str(x) for x in error.args]
    status_code = 500
    success = False
    response = {
        'success': success,
        'error': {
            'type': error.__class__.__name__,
            'message': message
        }
    }

    return jsonify(response), status_code


# Shut down the scedhuler when exiting the app
#atexit.register(lambda: stop())

if __name__ == '__main__':
    create_app().run()
