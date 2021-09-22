from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return "<User %r>" % self.id
    
    def serialize(self):
        return {
            'id':self.id,
            'firstname':self.firstname,
            'lastname':self.lastname,
            'password': self.password,
            'email': self.email
        }
    def serialize_just_username(self):
        return {
        'id': self.id,
        'firstname': self.firstname,
        'lastname':self.lastname
        }

class Vehicle(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    model = db.Column(db.String(50))
    manufacturer = db.Column(db.String(50))
    passengers = db.Column(db.String(30))
    vehicle_class = db.Column(db.String(50))
    favorite = db.relationship("Favorite",lazy=True)
    favorite_id = db.Column(db.Integer, db.ForeignKey('favorites.id'))

    def __repr__(self):
        return "<Vehicles %r>" % self.id
    
    def serialize(self):
        return {
            'id':self.id,
            'name':self.name,
            'model':self.model,
            'manufacturer': self.manufacturer,
            'passengers': self.passengers,
            'vehicle_class': self.vehicle_class
        }
    def serialize_just_vehicles(self):
        return {
        'id': self.id,
        'name': self.name,
        'model':self.model
        }

class Favorite(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(30))
    favorite_name = db.Column(db.String(50))
    user = db.relationship("User",backref=db.backref('user',lazy=True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "<Favorites %r>" % self.id
    
    def serialize(self):
        return {
            'id':self.id,
            'category':self.category,
            'favorite_name':self.favorite_name,
            'user_id':self.user_id
        }
    def serialize_just_favorites(self):
        return {
        'id': self.id,
        'category': self.category,
        'favorite_name':self.favorite_name
        }

class Character(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable=False)
    height = db.Column(db.Integer)
    birth_year = db.Column(db.String(30))
    gender = db.Column(db.String(30))
    favorite = db.relationship('Favorite',lazy=True)
    favorite_id = db.Column(db.Integer, db.ForeignKey('favorites.id'))

    def __repr__(self):
        return "<Characters %r>" % self.id

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'height': self.height,
            'birth_year': self.birth_year,
            'gender': self.gender,
        }

    def serialize_just_character(self):
        return {
        'id': self.id,
        'name': self.name,
        'gender':self.gender,
        }    

class Planet(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30), nullable=False)
    diameter = db.Column(db.Integer)
    climate = db.Column(db.String(30))
    terrain = db.Column(db.String(30))
    population = db.Column(db.String(30))
    favorite = db.relationship("Favorite",lazy=True)
    favorite_id = db.Column(db.Integer, db.ForeignKey('favorites.id'))

    def __repr__(self):
        return "<Planets %r>" % self.id
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'diameter': self.diameter,
            'climate': self.climate,
            'terrain': self.terrain,
            'population': self.population,
        }
    def serialize_just_planet(self):
        return {
        'id': self.id,
        'name': self.name,
        'terrain': self.terrain,
        }  