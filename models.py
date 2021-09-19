from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(30), nullable=False)
    lastname = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    isActive= db.Column(db.Boolean, default=False)

    def __repr__(self):
        return "<User %r>" % self.id
    
    def serialize(self):
        return {
            'id':self.id,
            'firstname':self.firstname,
            'lastname':self.lastname,
            'password': self.password,
            'email': self.email,
            'isActive': self.isActive
        }
    def serialize_just_username(self):
        return {
        'id': self.id,
        'firstname': self.firstname,
        'lastname':self.lastname
        }
