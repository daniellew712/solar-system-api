
from flask import Blueprint, request, Response
from ..models.planet import Planet
from .route_utilities import validate_model
from ..db import db

planets_bp = Blueprint("planets_bp", __name__, url_prefix = "/planets")

@planets_bp.post("")
def create_new_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)
    db.session.add(new_planet)
    db.session.commit()

    return new_planet.to_dict(), 201

@planets_bp.get("")
def get_all_planets():
    query = db.select(Planet)
    description_param = request.args.get("description")
    size_param = request.args.get("size")
    if description_param:
        query = query.where(Planet.description.ilike(f"%{description_param}%"))
    
    if size_param:
        query = query.where(Planet.size > size_param)
    
    query = query.order_by(Planet.size, Planet.id)
    
    planets = db.session.scalars(query)
    planets_response = []
    for planet in planets:
        planets_response.append(planet.to_dict())

    return planets_response
@planets_bp.get("/<id>")

def get_one_planet(id):
    planet = validate_model(Planet, id)
    
    return planet.to_dict()

@planets_bp.put("/<id>")
def update_planet(id):
    planet = validate_model(Planet, id)

    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.size = request_body["size"]
 
    db.session.commit()

    return Response(status = 204, mimetype = "application/json")

@planets_bp.delete("/<id>")
def delete_planet(id):
    planet = validate_model(Planet, id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status = 204, mimetype = "application/json")




    
