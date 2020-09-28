from http import HTTPStatus
from datetime import datetime

import logging
import json


class AppException(Exception):
    """ Base app exception """

    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_err_msg = 'App exception occurred'
    user_err_msg = 'We are sorry! Something happened on our end.'

    def __init__(self, *args, user_err_msg=None):
        print('App init called...')
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
            'type': type(self).__name__,
            'http_status': self.http_status,
            'message': self.args[0] if self.args else self.internal_err_msg,
            'args': self.args[1:]
        }

        logging.info(f'EXCEPTION - {datetime.now()}: {exception}')


class ProtectedDatasetError(AppException):
    """ An exception for a forbidden action on a protected component """

    def __init__(self, dataset_name=None, dataset_id=None, message=None):
        super().__init__(message)

        self.internal_err_msg = f'Dataset {dataset_name | dataset_id |  } cannot be sent!'


if __name__ == '__main__':

    raise ProtectedDatasetError('Dataset cannot be sent!')
