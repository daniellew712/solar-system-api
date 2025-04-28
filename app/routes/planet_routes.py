
from flask import Blueprint, abort, make_response, request, Response
from ..models.planet import Planet
from ..db import db

planets_bp = Blueprint("planets_bp", __name__, url_prefix = "/planets")

@planets_bp.post("")
def create_new_planet():
    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    size = request_body["size"]

    new_planet = Planet(name=name, description=description, size = size)
    db.session.add(new_planet)
    db.session.commit()

    response = {
        "id": new_planet.id,
        "name": new_planet.name,
        "description": new_planet.description,
        "size": new_planet.size
    }
    return response, 201

@planets_bp.get("")
def get_all_planets():
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.scalars(query)
    planets_response = []
    for planet in planets:
        planets_response.append(
            {
                "id": planet.id, 
                "name": planet.name, 
                "description": planet.description, 
                "size": planet.size
            }
        )
    return planets_response
@planets_bp.get("/<id>")

def get_one_planet(id):
    planet = validate_planet(id)
    
    return {
        "id" : planet.id,
        "name" : planet.name,
        "description" : planet.description,
        "size " : planet.size 
    }

@planets_bp.put("/<id>")
def update_planet(id):
    planet = validate_planet(id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.size = request_body["size"]
    db.session.commit()

    return Response(status = 204, mimetype = "application/json")

@planets_bp.delete("/<id>")
def delete_planet(id):
    planet = validate_planet(id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status = 204, mimetype = "application/json")





# @planets_bp.get("/<id>")

# def get_one_planet(id):
#     planet = validate_planet(id)
#     planet_response = dict(
#         id = planet.id,
#         name = planet.name,
#         description = planet.description,
#         size = planet.size
#     )
#     return planet_response

def validate_planet(id):
    try: 
        id = int(id)
    except: 
        #invalid = {"message": f"planet id {id} is invalid."}
        abort(make_response({"message": f"planet id {id} is invalid."}, 400))

    query = db.select(Planet).where(Planet.id == id)
    planet = db.session.scalar(query)
    if not planet:
        abort(make_response({"message": f"planet id {id} is not found."}, 404))
    return planet
    
