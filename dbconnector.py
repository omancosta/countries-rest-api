# -*- encoding: utf-8 -*-

import sqlite3
import json
from collections import OrderedDict
from sqlite3 import Error

def connect():
    try:
        connection = sqlite3.connect('countries.db')
        return connection
    except Error as e:
        print(e)
    return None

def all_countries():
    return search_countries()

def get_country_by_id(id):
    return search_countries(id)

def search_countries(id=-1):
    connection = connect()
    if connection is not None:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        sqlStr = "SELECT * FROM countries"
        if id != -1:
            sqlStr += " WHERE id =" + str(id)
        cursor.execute(sqlStr)
        countries = cursor.fetchall()
        connection.commit()
        connection.close()
        return json.dumps([OrderedDict(ix) for ix in countries])
    return None