import os 
from flask import Flask,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from models import db,User,Vehicle,Character,Planet,Favorite
from flask_migrate import Migrate
import flask_excel as excel
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
    
@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        return jsonify({"result": request.get_array(field_name='file')})
    return '''
    <!doctype html>
    <title>Upload an excel file</title>
    <h1>Excel file upload (csv, tsv, csvz, tsvz only)</h1>
    <form action="" method=post enctype=multipart/form-data><p>
    <input type=file name=file><input type=submit value=Upload>
    </form>
    '''
    
@app.route("/user",methods=["POST","GET"])
def user():
    if request.method == "GET":
        user = User.query.all()
        user = list(map(lambda x: x.serialize(), user))
        return jsonify(user)
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
        vehicles = Vehicle.query.get(1)
        if vehicles is not None:
            return jsonify(vehicles.serialize())   
    else:
        vehicles = Vehicle()
        data = request.json.get("name")
        vehicles.name = request.json.get("name")
        vehicles.model = request.json.get("model")
        vehicles.manufacturer = request.json.get("manufacturer")
        vehicles.passengers = request.json.get("passengers")
        vehicles.vehicle_class = request.json.get("vehicle_class")
        
        db.session.add(vehicles)
        db.session.commit()
    

    return jsonify(vehicles.serialize()),200

@app.route("/characters",methods=["POST","GET"])
def characters():
    if request.method == "GET":
        characters = Character.query.all()
        characters = list(map(lambda x: x.serialize(), characters))
        return jsonify(characters)
        if characters is not None:
            return jsonify(characters.serialize())   
    else:
        characters = Character()
        data = request.json.get("name")
        characters.name = request.json.get("name")
        characters.height = request.json.get("height")
        characters.birth_year = request.json.get("birth_year")
        characters.gender = request.json.get("gender")
        
        db.session.add(characters)
        db.session.commit()
    

    return jsonify(characters.serialize()),200

@app.route("/planets",methods=["POST","GET"])
def planets():
    if request.method == "GET":
        planets = Planet.query.get(1)
        if planets is not None:
            return jsonify(planets.serialize())   
    else:
        planets = Planet()
        data = request.json.get("name")
        planets.name = request.json.get("name")
        planets.diameter = request.json.get("diameter")
        planets.climate = request.json.get("climate")
        planets.terrain = request.json.get("terrain")
        planets.population = request.json.get("population")
        
        db.session.add(planets)
        db.session.commit()
    

    return jsonify(planets.serialize()),200

@app.route("/favorites",methods=["POST","GET"])
def favorites():
    if request.method == "GET":
        favorites = Favorite.query.all()
        favorites = list(map(lambda x: x.serialize(), favorites))
        return jsonify(favorites)
        if favorites is not None:
            return jsonify(favorites.serialize())   
    else:
        favorites = Favorite()
        data = request.json.get("favorite_name")
        favorites.category=request.json.get("category")
        favorites.favorite_name=request.json.get("favorite_name")
        favorites.user_id=request.json.get("user_id")
        db.session.add(favorites)
        db.session.commit()
    

    return jsonify(favorites.serialize()),200


@app.route("/favorites/<int:id>",methods=["POST","GET"])
def favorite_list(id):
    if request.method == "GET":
        if id is not None:
            favorites = Favorite.query.get(id)
            return jsonify(favorites.serialize())
        else:
            return jsonify('Missing id for route'),404   
    

if __name__ == "__main__":
    app.run(host='localhost',port=8080)




