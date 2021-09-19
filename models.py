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

class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    model = db.Column(db.String(50))
    manufacturer = db.Column(db.String(50))
    passengers = db.Column(db.String(30))
    vehicle_class = db.Column(db.String(50))

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

class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(30))
    favorite_name = db.Column(db.String(50))

    def __repr__(self):
        return "<Favorites %r>" % self.id
    
    def serialize(self):
        return {
            'id':self.id,
            'category':self.category,
            'favorite_name':self.favorite_name
        }
    def serialize_just_favorites(self):
        return {
        'id': self.id,
        'category': self.category,
        'favorite_name':self.favorite_name
        }
