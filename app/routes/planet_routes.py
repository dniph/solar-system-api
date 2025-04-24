from flask import abort, Blueprint, make_response
# from app.models.planet import planets

planet_bp = Blueprint("plabet_bp", __name__, url_prefix="/planets")

#Validations
# def validate_planet(planet_id):
#     try:
#         planet_id = int(planet_id)
#     except ValueError:
#         invalid_error = {"message": f"Planet {planet_id} invalid"}
#         abort(make_response(invalid_error, 400))
    
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
