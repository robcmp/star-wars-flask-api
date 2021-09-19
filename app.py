import os 
from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from models import db,User,Vehicles
from flask_migrate import Migrate
#from flask_script import Manager

BASEDIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= "sqlite:///" + os.path.join(BASEDIR,"test.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['ENV'] = 'development'
app.config['DEBUG'] = True

#manager = Manager(app)

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def home():
    return jsonify('Hola Mundo')
    
@app.route("/user",methods=["POST","GET"])
def user():
    if request.method == "GET":
        user = User.query.get(1)
        if user is not None:
            return jsonify(user.serialize())   
    else:
        user = User()
        data = request.json.get("firstname")
        user.firstname = request.json.get("firstname")
        user.lastname = request.json.get("lastname")
        user.password = request.json.get("password")
        user.email = request.json.get("email")
        
        db.session.add(user)
        db.session.commit()
    

    return jsonify(user.serialize()),200

@app.route("/vehicles",methods=["POST","GET"])
def vehicles():
    if request.method == "GET":
        vehicles = Vehicles.query.get(1)
        if vehicles is not None:
            return jsonify(vehicles.serialize())   
    else:
        vehicles = Vehicles()
        data = request.json.get("name")
        vehicles.name = request.json.get("name")
        vehicles.model = request.json.get("model")
        vehicles.manufacturer = request.json.get("manufacturer")
        vehicles.passengers = request.json.get("passengers")
        vehicles.vehicle_class = request.json.get("vehicle_class")
        
        db.session.add(vehicles)
        db.session.commit()
    

    return jsonify(vehicles.serialize()),200

@app.route("/character",methods=["POST","GET"])
def character():
    if request.method == "GET":
        character = Character.query.get(1)
        if character is not None:
            return jsonify(character.serialize())   
    else:
        character = Character()
        data = request.json.get("name")
        character.name = request.json.get("name")
        character.height = request.json.get("height")
        character.birth_year = request.json.get("birth_year")
        character.gender = request.json.get("gender")
        
        db.session.add(character)
        db.session.commit()
    

    return jsonify(character.serialize()),200

@app.route("/planet",methods=["POST","GET"])
def planet():
    if request.method == "GET":
        planet = Planet.query.get(1)
        if planet is not None:
            return jsonify(planet.serialize())   
    else:
        planet = Planet()
        data = request.json.get("name")
        planet.name = request.json.get("name")
        planet.diameter = request.json.get("diameter")
        planet.climate = request.json.get("climate")
        planet.terrain = request.json.get("terrain")
        planet.population = request.json.get("population")
        
        db.session.add(planet)
        db.session.commit()
    

    return jsonify(planet.serialize()),200


if __name__ == "__main__":
    app.run(host='localhost',port=8080)




