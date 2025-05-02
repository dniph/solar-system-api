from flask import Blueprint, abort,make_response,request,Response
# from app.models.book import planet
from app.models.planet import Planet
from ..db import db


planet_bp = Blueprint("planet_bp", __name__, url_prefix="/planets")


@planet_bp.post("")
def create_planet():
    request_body = request.get_json()
    name = request_body["name"]
    description = request_body["description"]
    distance_from_sun = request_body["distance_from_sun"]
    
    new_planet = Planet(name=name, description=description, distance_from_sun=distance_from_sun )
    db.session.add(new_planet)
    db.session.commit()
    
    response = dict(
            id = new_planet.id,
            name = new_planet.name,
            description = new_planet.description,
            distance_from_sun = new_planet.distance_from_sun
            )
    return response, 201


@planet_bp.get("")
def get_all_planets():
    query = db.select(Planet).order_by(Planet.id)
    planets = db.session.scalars(query)
    # We could also write the line above as:
    # books = db.session.execute(query).scalars()

    planets_response = []
    for planet in planets:
        planets_response.append(dict(
            id = planet.id,
            name = planet.name,
            description = planet.description,
            distance_from_sun = planet.distance_from_sun
            
            ))
    return planets_response

@planet_bp.get("/<planet_id>")
def get_one_book(planet_id):
    planet = validate_planet(planet_id)

    return dict(
            id = planet.id,
            name = planet.name,
            description = planet.description,
            distance_from_sun = planet.distance_from_sun
            
            )

def validate_planet(planet_id):
    try:
        planet_id = int(planet_id)
    except:
        response = {"message": f"planet {planet_id} invalid"}
        abort(make_response(response , 400))

    query = db.select(Planet).where(Planet.id == planet_id)
    planet = db.session.scalar(query)
    
    if not planet:
        response = {"message": f"planet {planet_id} not found"}
        abort(make_response(response, 404))

    return planet
    
    
@planet_bp.put("/<planet_id>")
def update_planet(planet_id):
    planet = validate_planet(planet_id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["description"]
    planet.distance_from_sun = request_body["distance_from_sun"]
    db.session.commit()

    return Response(status=204, mimetype="application/json")

@planet_bp.delete("/<planet_id>")
def delete_book(planet_id):
    planet = validate_planet(planet_id)
    db.session.delete(planet)
    db.session.commit()

    return Response(status=204, mimetype="application/json")