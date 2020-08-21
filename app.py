from config import config

from flask import Flask, jsonify, make_response, render_template, send_from_directory
from flasgger import Swagger

import logging
import os


app = Flask(__name__)

swagger_config = Swagger.DEFAULT_CONFIG
swagger_config['specs_route'] = '/api/docs'

swagger = Swagger(app, config=swagger_config)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/simple')
def simple():
    return render_template('simple.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/favicon.ico')
def favicon():
    """
    Returns a favicon.
    """

    url = os.path.join(app.root_path, 'static/favicon')

    return send_from_directory(url, 'favicon.ico')


@app.errorhandler(404)
def not_found():

    logging.error('Resource not found...')

    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':

    logging.info('Running __main__...')

    # Ensure to set debug=False BEFORE deploying to production
    app.run(host='0.0.0.0', port='8000', debug=config['flask_debug'])