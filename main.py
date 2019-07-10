import logging
import logging.config
import json

from flask import escape
from flask import abort

from logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

from config import CONFIG


def main(request):
    bot_name = CONFIG['bot_name'].get()
    
    if request is None:
        logger.info('Hi, I\'m %s!', bot_name)
        return 'OK'
    
    logger.info('Bot %s is alive!', bot_name)


    content_type = request.headers['content-type']
    if content_type == 'application/json':
        bitbucket_event = request.get_json(silent=True)
    else:
        raise ValueError("Unknown content type: {}".format(content_type))

    r = json.dumps(bitbucket_event, indent=2)
    logger.info(r)
    return r


if __name__ == '__main__':
    main(None)
