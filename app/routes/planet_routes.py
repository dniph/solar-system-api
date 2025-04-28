from flask import abort, Blueprint, make_response, request, Response
from ..db import db
from app.models.planet import Planet


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

    planets_response = []
    
    for planet in planets:
        planets_response.append(dict(
            id = planet.id,
            name = planet.name,
            description = planet.description,
            distance_from_sun = planet.distance_from_sun
            
            ))
        
    return planets_response

@planet_bp.get("/<id>")
def get_one_planet(id):
    planet = validate_planet(id)
    return dict(
        id = planet.id,
            name = planet.name,
            description = planet.description,
            distance_from_sun = planet.distance_from_sun 
        )

@planet_bp.put("/<id>")
def update_planet(id):
    planet = validate_planet(id)
    request_body = request.get_json()

    planet.name = request_body["name"]
    planet.description = request_body["color"]
    planet.distance_from_sun = request_body["personality"]

    db.session.commit()
    return Response(status=204, mimetype="application/json")

@planet_bp.delete("/<id>")
def delete_planet(id):
    planet = validate_planet(id)
    db.session.delete(planet)
    db.session.commit()
    return Response(status=204, mimetype="application/json")

#Validations
def validate_planet(id):
    try:
        id = int(id)
    except ValueError:
        invalid_error = {"message": f"Planet {id} invalid"}
        abort(make_response(invalid_error, 400))
    
    query = db.select(Planet).where(Planet.id == id)
    planet = db.session.scalar(query)
    
    if not planet:
        not_found = {"message":f"Planet id ({id}) is invalid."}
        abort(make_response(not_found, 404))
    return planet
    
#     for planet in planets:
#         if planet.id == planet_id:
#             return planet
    
#     not_found = {"message": f"Planet {planet_id} not found"}
#     abort(make_response(not_found, 404))

# #Get all planets
# @planet_bp.get("")
# def get_all_planets():
#     planets_response = []
#     for planet in planets:
#         planets_response.append(dict(
#             id = planet.id,
#             name = planet.name,
#             description = planet.description,
#             distance_from_sun = planet.distance_from_sun
            
#         ))
    
#     return planets_response


# #Get one planet 
# @planet_bp.get("/<planet_id>")
# def get_one_planet(planet_id):
#     planet = validate_planet(planet_id)

#     return dict(id = planet.id,
#         name = planet.name,
#         description = planet.description,
#         distance_from_sun = planet.distance_from_sun
#         )
