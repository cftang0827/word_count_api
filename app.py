from flask import Flask, jsonify

from controllers import controller

app = Flask(__name__)
app.run(port=5000, debug=True)


@app.route('/wordcount')
def wordcount():
    return jsonify()
