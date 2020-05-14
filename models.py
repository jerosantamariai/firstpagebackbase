from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Users (db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=True)
    lastname = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=False)

    def serialize(self):
        return{
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'name': self.name,
            'lastname': self.lastname,
            'email': self.email,
        }