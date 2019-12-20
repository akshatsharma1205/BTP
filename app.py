from flask import Flask, jsonify
import json
from flask_sqlalchemy import SQLAlchemy
from flask import request
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from flask_cors import CORS

CORS(app)


from models import *


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)


@app.route("/add")
def add_c():
    lon=request.args.get('lon')
    lat=request.args.get('lat')

    try:
        cordi=Result(
            lon=lon,
            lat=lat
        )
        db.session.add(cordi)
        db.session.commit()
        return "Location added. coordinate id={}".format(cordi.id)
    except Exception as e:
	    return(str(e))

@app.route("/getall")
def get_all():
    try:
        books=Result.query.all()
        #[e.serialize() for e in books] 
        #longi = float(books[-1].serialize()[1])
        #lati = float(books[-1].serialize()[2])
        print(type(books[-1].serialize()))
        a = books[-1].serialize()
        a_lon = float(a["lon"])
        a_lat = float(a["lat"])
        #return a["lon"]
        var = {"geometry": {"type": "Point", "coordinates": [a_lat, a_lon]}, "type": "Feature", "properties": {}}
        var = json.dumps(var)
        print(type(var))
        return (var)
    except Exception as e:
	    return(str(e))


if __name__ == '__main__':
    app.run()
