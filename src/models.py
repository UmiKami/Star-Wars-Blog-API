from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=True, default=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Userr(db.Model):
    __tablename__ = 'Userr'

    id = db.Column(db.Integer, primary_key=True)
    USER_FNAME = db.Column(db.String(250), nullable=False)
    USER_LNAME = db.Column(db.String(250), nullable=False)
    USER_EMAIL = db.Column(db.String(250), nullable=False)
    USER_PASSWORD = db.Column(db.String(250), nullable=False)
    USER_FAVORITE_LIST = db.Column(db.Integer, db.ForeignKey("Favorites_List.id"))

    def __repr__(self):
        return '<Userr %r>' % self.userrname

class Favorites_List(db.Model):
    __tablename__ = 'Favorites_List'

    id = db.Column(db.Integer, primary_key=True)
    USER_ID = db.Column(db.Integer, db.ForeignKey('Userr.id'))
    FAV_CHARACTER = db.Column(db.Integer, db.ForeignKey('Character.id'))
    FAV_PLANET = db.Column(db.Integer, db.ForeignKey('Planet.id'))
    user = db.relationship("Userr", foreign_keys=[USER_ID])
    favoriteChar = db.relationship("Character", foreign_keys=[FAV_CHARACTER])
    favoritePlanet = db.relationship("Planet", foreign_keys=[FAV_PLANET])

    def __repr__(self):
        return '<Favorites_List %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "favorite_character": self.FAV_CHARACTER,
            "favorite_planet": self.FAV_PLANET,
            # do not serialize the password, its a security breach
        }


class Planet(db.Model):
    __tablename__ = 'Planet'

    id = db.Column(db.Integer, primary_key=True)
    PLANET_NAME = db.Column(db.String(250))
    PLANET_ROT_PERIOD = db.Column(db.Integer)
    PLANET_TRANS_PERIOD = db.Column(db.Integer)
    PLANET_DIAMETER = db.Column(db.Integer)
    PLANET_CLIMATE = db.Column(db.String(250))
    PLANET_GRAVITY = db.Column(db.String(250))
    PLANET_TERRAIN = db.Column(db.String(250))
    PLANET_SURFACE_WATER = db.Column(db.Integer)
    PLANET_POP = db.Column(db.Integer)

    def __repr__(self):
        return '<Planet %r>' % self.PLANET_NAME

    def serialize(self):
        return {
            "id": self.id,
            "planet_name": self.PLANET_NAME,
            "planet_pop": self.PLANET_POP,
            "planet_terrain": self.PLANET_TERRAIN,
            # do not serialize the password, its a security breach
        }

class Character(db.Model):
    __tablename__ = 'Character'

    id = db.Column(db.Integer, primary_key=True)
    CHAR_NAME = db.Column(db.String(250))
    CHAR_SPECIES = db.Column(db.String(250))
    CHAR_GENDER = db.Column(db.String(250))
    CHAR_YOB = db.Column(db.String(250))
    CHAR_HEIGHT = db.Column(db.Integer)
    CHAR_WEIGHT = db.Column(db.Integer)
    CHAR_EYE_COLOR = db.Column(db.String(250))
    CHAR_HAIR_COLOR = db.Column(db.String(250))
    CHAR_SKIN_COLOR = db.Column(db.String(250))

    def __repr__(self):
        return '<Character %r>' % self.CHAR_NAME

    def serialize(self):
        return {
            "id": self.id,
            "species": self.CHAR_SPECIES,
            "name": self.CHAR_NAME,
            "gender": self.CHAR_GENDER
            # do not serialize the password, its a security breach
        }
