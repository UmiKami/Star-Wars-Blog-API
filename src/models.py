from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    USER_FNAME = db.Column(db.String(250), nullable=False)
    USER_LNAME = db.Column(db.String(250), nullable=False)
    USER_EMAIL = db.Column(db.String(250), nullable=False)
    USER_PASSWORD = db.Column(db.String(250), nullable=False)   
    favorites = db.relationship('Favorites_List')

    def __repr__(self):
        return self.USER_EMAIL + '-' + str(self.id)
    
    def serialize(self):
        return {
            "id": self.id,
            "first_name": self.USER_FNAME,
            "last_name": self.USER_LNAME,
            "email": self.USER_EMAIL,
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
class Favorites_List(db.Model):
    __tablename__ = 'Favorites_List'

    id = db.Column(db.Integer, primary_key=True)
    USER_ID = db.Column(db.Integer, db.ForeignKey('User.id'))
    FAV_CHARACTER_ID = db.Column(db.Integer, db.ForeignKey('Character.id'))
    FAV_PLANET_ID = db.Column(db.Integer, db.ForeignKey(Planet.id))
    user = db.relationship("User", foreign_keys=[USER_ID])
    character = db.relationship('Character')
    planet = db.relationship('Planet')

    def __repr__(self):
        return '<Favorites_List %r>' % self.id

    def serialize(self):
        planet = None
        character = None
        if self.planet is not None:
            planet=self.planet.serialize()
        if self.character is not None:
            character = self.character.serialize()

        return {
            "id": self.id,
            "user_id":self.USER_ID,
            "planet": planet,
            "character": character,
            # do not serialize the password, its a security breach
        }