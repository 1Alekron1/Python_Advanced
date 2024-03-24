import logging
import json


class JsonAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        json_msg = json.dumps(msg, ensure_ascii=False)
        json_msg = json_msg.replace('"', '\"')
        return json_msg, kwargs


logging.basicConfig(filename='skillbox_json_messages.log', level=logging.INFO,
                    format='{"time": "%(asctime)s", "level": "%(levelname)s", "message": %(message)s}')

logger = JsonAdapter(logging.getLogger(__name__))

logger.info('Hello, world!')
logger.warning('{"key": "value"}\n')
