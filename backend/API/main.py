import json
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hey"


@app.route('/api/data/<file_name>')
def get_api_data(file_name):
    try:
        json_file = open('../data/json/data.{}.json'.format(file_name))
        json_data = json.load(json_file)
        json_file.close()
        return jsonify(json_data)
    except OSError:
        return 'No data found'


app.run()
