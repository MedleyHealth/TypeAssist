from enum import Enum
from http import HTTPStatus
from datetime import datetime

import logging
import json

class JobStatus(Enum):
    READY = (1, 'Job is ready!')
    PENDING = (2, 'Job is pending!')
    IN_PROGRESS = (3, 'Job is in progress!')
    FINISHED = (4, 'Job is finished!')

    def __new__(cls, member_value, member_phrase):
        member = object.__new__(cls)

        member._value_ = member_value
        member.phrase = member_phrase

        return member


class APIException(Exception):
    """ Base API exception """

    http_status = HTTPStatus.INTERNAL_SERVER_ERORR
    internal_err_msg = 'API Exception occurred'
    user_err_msg = 'We are sorry! Something happened on our end.'

    def __init__(self, *args, user_err_msg=None):
        if args:
            self.internal_err_msg = args[0]
            super().__init__(*args)
        else:
            super().__init__(self.internal_err_msg)

        if user_err_msg is not None:
            self.user_err_msg = user_err_msg

    def to_json(self):
        err = {'http_status': self.http_status, 'user_err_msg': self.user_err_msg}

        return json.dumps(err)

    def log_exception(self):

        exception = {
            'type': type(self).__name__
            'http_status': self.http_status,
            'message': self.args[0] if self.args else self.internal_err_msg,
            'args': self.args[1:]
        }

        logging.info(f'EXCEPTION - {datetime.now()}: {exception}')
