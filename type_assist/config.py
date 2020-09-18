import logging
import yaml
import sys
import io
import os


class Configure:
    """
    Configures the behavior of the Type Assist application

    :param config_path: A string path to the configuration YML file
    """

    def __init__(self, config_path=None):
        if config_path is None:
            self.config_path = '../config.yml'
        self.config = self.load_config(config_path)

    @staticmethod
    def load_config(config_path):
        """
        Loads the app configuration

        :param config_path: The path to the configuration YML file
        :return config: A nested dictionary of configuration parameters
        """

        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
        return config


config = Configure.load_config()

if not os.path.exists('logs/'):
    os.makedirs('logs/')

# Create logging handlers for files and stdout
log_level = getattr(logging, config['log_level'])
log_handler = logging.FileHandler(filename='logs/debug.log')

stdout_level = getattr(logging, config['stdout_level'])
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setLevel(stdout_level)

handlers = [
    log_handler,
    stdout_handler
]

# Configure the log settings
logging.basicConfig(
    level=log_level,
    format='%(asctime)s.%(msecs)03d %(filename)24s:%(lineno)-5s %(levelname)-8s %(message)s',
    datefmt='%m-%d-%y %H:%M:%S',
    handlers=handlers
)

logging.info('Loaded configuration...')
logging.debug('Config parameters:' + str(config))

# Enable/disable print statements
if config['allow_print']:
    sys.stdout = sys.__stdout__
else:
    logging.warning('Suppressing print statements.')
    sys.stdout = io.StringIO()
