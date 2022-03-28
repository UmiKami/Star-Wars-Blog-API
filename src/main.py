"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
import json
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Character, Planet, Favorites_List, User
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# @app.route('/user', methods=['GET'])
# def handle_hello():

#     users = User.query.all()
#     all_users = list(map(lambda x: x.serialize(), users))

#     return jsonify(all_users), 200
# @app.route('/user', methods=['POST'])
# def create_user():

#     request_body_user = request.get_json()
#     user1 = User(first_name=request_body_user["first_name"], email=request_body_user["email"], password=request_body_user["password"])
#     db.session.add(user1)
#     db.session.commit()

#     return jsonify(request_body_user), 200

@app.route('/people', methods=['GET'])
def getPeople():
    people = Character.query.all()
    all_people = list(map(lambda x: x.serialize(), people))

    return jsonify(all_people), 200


@app.route('/planets', methods=["GET"])
def getPlanets():
    planets = Planet.query.all()

    all_planets = list(map(lambda x: x.serialize(), planets))

    return jsonify(all_planets), 200

@app.route('/users', methods=['GET'])
def getUsers():
    users = User.query.all()
    all_users = list(map(lambda x: x.serialize(), users))

    return jsonify(all_users)

@app.route('/users/favorites', methods=['GET'])
def getUserFavorites():
    favorites = Favorites_List.query.all()
    all_favorites = list(map(lambda x: x.serialize(), favorites))

    return jsonify(all_favorites)
@app.route('/users/favorites/people/<int:people_id>', methods=['POST'])
def postUserFavoriteChar(people_id):
    request_body_user = request.get_json()
    favorite = Favorites_List(USER_ID=request_body_user["user_id"], FAV_CHARACTER_ID=people_id)
    db.session.add(favorite)
    db.session.commit()

    return jsonify(request_body_user), 200
@app.route('/users/favorites/planet/<int:planet_id>', methods=['POST'])
def postUserFavoritePlanet(planet_id):
    request_body_user = request.get_json()
    favorite = Favorites_List(USER_ID=request_body_user["user_id"], FAV_PLANET_ID=planet_id)
    db.session.add(favorite)
    db.session.commit()

    return jsonify(request_body_user), 200

# DELETE

@app.route('/users/favorites/people/<int:people_id>', methods=['DELETE'])
def deleteUserFavoriteChar(people_id):
    favChar = Favorites_List.query.filter_by(FAV_CHARACTER_ID = people_id).first()
    db.session.delete(favChar)
    db.session.commit()

    return "Succesfully deleted", 200

@app.route('/users/favorites/planet/<int:planet_id>', methods=['DELETE'])
def deleteUserFavoritePlanet(planet_id):
    favPlanet = Favorites_List.query.filter_by(FAV_PLANET_ID = planet_id).first()
    db.session.delete(favPlanet)
    db.session.commit()

    return "Succesfully deleted", 200

#####################################################################
### Example code ###   

# @app.route('/people', methods=['POST'])
# def setPeople():
#     request_body_people = request.get_json()
#     person = Character(CHAR_NAME=request_body_people["name"], CHAR_SPECIES=request_body_people["species"], CHAR_GENDER=request_body_people["gender"])
#     db.session.add(person)
#     db.session.commit()

#     return jsonify(request_body_people), 200

# @app.route('/people/<int:people_id>', methods=['GET'])
# def getPerson(people_id):
#     person = Character.query.get(people_id)
#     if person is None:
#         raise APIException('User not found', status_code=404)    
#     payload = {
#         "msg": "This is the person!",
#         "person": person.serialize() 
#     }

#     return jsonify(payload), 200
# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
