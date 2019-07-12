import os
import logging
import logging.config
import json
import requests

from flask import escape
from flask import abort

from logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

from config import CONFIG
from bitbucket2chat import handle_bitbucket_event


def main(request):
    bot_name = CONFIG['bot_name'].get()
    
    if request is None:
        logger.info('Hi, I\'m %s!', bot_name)
        return 'OK'
    
    logger.info('Bot %s is alive!', bot_name)

    if request.headers.get('User-Agent') == 'Bitbucket-Webhooks/2.0':
        event = request.get_json(silent=True)
        headers = request.headers

        chat_response_payload = handle_bitbucket_event(event, headers)
        
        # Skip successful commits for now.
        if 'is *SUCCESSFUL*.' in chat_response_payload:
            return '200'
        
        response = send_to_chat(chat_response_payload)
        logger.info('Response from chat. Code=%s, Text=%s', response.status_code, response.text)
        return '{} {}'.format(response.status_code, response.text)
    else:
        return abort(400)

def send_to_chat(chat_response_payload):
    webhook_url = os.getenv('CHAT_WEBHOOK_URL')

    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

    response = requests.post(
        webhook_url, data=chat_response_payload, headers=message_headers)

    return response


if __name__ == '__main__':
    main(None)
