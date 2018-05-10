import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#Test Countries
countries= [
    {
        "id": 1,
        "name": "Germany",
        "capital": "Berlin",
        "altSpellings": [
            "DE",
            "Federal Republic of Germany",
            "Bundesrepublik Deutschland"
        ],
        "relevance": "3",
        "region": "Europe",
        "subregion": "Western Europe",
        "translations": {
            "de": "Deutschland",
            "es": "Alemania",
            "fr": "Allemagne",
            "it": "Germania"
        },
        "population": 81083600,
        "latlng": [
            51.0,
            9.0
        ],
        "demonym": "German",
        "area": 357114.0,
        "gini": 28.3,
        "timezones": [
            "UTC+01:00"
        ],
        "borders": [
            "AUT",
            "BEL",
            "CZE",
            "DNK",
            "FRA",
            "LUX",
            "NLD",
            "POL",
            "CHE"
        ],
        "nativeName": "Deutschland",
        "callingCodes": [
            "49"
        ],
        "topLevelDomain": [
            ".de"
        ],
        "alpha2Code": "DE",
        "alpha3Code": "DEU",
        "currencies": [
            "Euro"
        ],
        "languages": [
            "de"
        ]
    }
]

@app.route('/', methods=['GET'])
def home():
    return "It is working :)"

@app.route('/api/countries/all', methods=['GET'])
def countries_all():
    return jsonify(countries);

@app.route('/api/country', methods=['GET'])
def get_country_id():
    result = []
    id = -1

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "[ERROR] Please specify the id."

    for country in countries:
        if country['id'] == id:
            result.append(country)
            break
    return jsonify(result)

app.run()