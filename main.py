from flask import Flask

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fsghfsdjkhgsd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.INTEGER, nullable=False)
    isActive = db.Column(db.BOOLEAN, default=True)

    def __repr__(self):
        return self.title


class Users(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    hash_password = db.Column(db.String, nullable=False)

