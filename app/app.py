from flask import Flask, jsonify, request
import logging
from datetime import datetime

from controllers import controller

app = Flask(__name__)

word_counter = controller.WordCounter()

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    app.logger.error("Page Not Found: {}".format(request.url))
    resp = jsonify(message)
    resp.status_code = 404

    return resp


@app.errorhandler(Exception)
def internal_error(e):
    message = {
        'status': 500,
        'message': 'Internal Server Error, Error Message: {}'.format(str(e))
    }
    app.logger.error("Internal Server Error, Error Message: {}".format(str(e)))
    resp = jsonify(message)
    resp.status_code = 500

    return resp

@app.route('/wordcount', methods=['POST'])
def wordcount():
        if request.method == 'POST':
            word = request.form['word']
            url = request.form['url']
            result = word_counter.count_from_url(url, word)
            result.update({
                "status": "ok"
            })
            resp = jsonify(result)
        else:
            raise Exception("Not A Valid Post Request")
        
        return resp

if __name__ == '__main__':
    handler = logging.FileHandler('./log/log_{}.log'.format(datetime.utcnow().strftime('%b_%d_%y_%H_%M_%S')))
    handler.setLevel(logging.DEBUG)
    logging_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)
    app.run(port=8000)
