import logging
from datetime import datetime

from flask import Flask, jsonify, request

from controllers import controller

app = Flask(__name__)

word_counter = controller.WordCounter()


@app.errorhandler(Exception)
def unhandle_error(e):
    message = {
        'message': 'Error Message: {}'.format(str(e)),
    }
    status_str = str(e).split(' ')[0]
    app.logger.error("Error Message: {}".format(str(e)))

    if status_str.isdigit():
        status_code = int(status_str)
    else:
        status_code = 500
    message.update({"status": status_code})

    resp = jsonify(message)
    resp.status_code = status_code

    return resp


@app.route('/wordcount', methods=['POST'])
def wordcount():
    if request.method == 'POST':
        word = request.form['word']
        url = request.form['url']
        result = word_counter.count_from_url(url, word)
        result.update({"status": "ok"})
        app.logger.info("Response ok")
        resp = jsonify(result)

        return resp


if __name__ == '__main__':
    handler = logging.FileHandler('./log/log_{}.log'.format(
        datetime.utcnow().strftime('%b_%d_%y_%H_%M_%S')))
    logging_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s'
    )
    handler.setFormatter(logging_format)
    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run(port=8000)
