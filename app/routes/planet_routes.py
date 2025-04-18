
from flask import Blueprint, abort, make_response
from ..models.planet import planets

planets_bp = Blueprint("planets_bp", __name__, url_prefix = "/planets")


@planets_bp.get("")
def get_all_planets():
    result_planets = []
    for planet in planets:
        result_planets.append(dict(id = planet.id, name =planet.name, description=planet.description, size = planet.size))
    return result_planets

@planets_bp.get("/<id>")

def get_one_planet(id):
    planet = validate_planet(id)
    planet_response = dict(
        id = planet.id,
        name = planet.name,
        description = planet.description,
        size = planet.size
    )
    return planet_response

def validate_planet(id):
    try: 
        id = int(id)
    except: 
        #invalid = {"message": f"planet id {id} is invalid."}
        abort(make_response({"message": f"planet id {id} is invalid."}, 400))
    
    for planet in planets:
        if planet.id == id:
            return planet
    abort(make_response({"message": f"planet id {id} is not found."}, 404))
