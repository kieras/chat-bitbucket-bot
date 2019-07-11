import logging
import logging.config
import json

from flask import escape
from flask import abort

from logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

from config import CONFIG
from bitbucket import handle_bitbucket_event


def main(request):
    bot_name = CONFIG['bot_name'].get()
    
    if request is None:
        logger.info('Hi, I\'m %s!', bot_name)
        return 'OK'
    
    logger.info('Bot %s is alive!', bot_name)

    if request.headers.get('User-Agent') == 'Bitbucket-Webhooks/2.0':
        response = handle_bitbucket_event(request)
        return response
    else:
        return abort(400)


if __name__ == '__main__':
    main(None)
