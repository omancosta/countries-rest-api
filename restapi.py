# -*- encoding: utf-8 -*-

import flask
from flask import request, jsonify
import dbconnector as dbconn

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "It is working :)"

@app.route('/api/countries/all', methods=['GET'])
def countries_all():
    return jsonify(dbconn.all_countries());

@app.route('/api/country', methods=['GET'])
def get_country_id():
    if 'id' in request.args:
        id = int(request.args['id'])
        return jsonify(dbconn.get_country_by_id(id))
    else:
        return "[ERROR] Please specify the id."

app.run()