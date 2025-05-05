from app import create_app, db 
from app.models.planet import Planet

my_app = create_app()
with my_app.app_context():
    
    db.session.add(Planet(name= "Mercury", description="The smallest and closest planet to the Sun", distance_from_sun="57.9")),
    db.session.add(Planet(name= "Venus", description="Similar in size to Earth, but with a toxic atmosphere.", distance_from_sun="108.2")),
    db.session.add(Planet(name= "Earth", description="Our home planet, the only known one with life.", distance_from_sun="149.6")),
    db.session.add(Planet(name= "Mars", description="The Red Planet, known for its dusty, rocky surface.", distance_from_sun="227.9")),
    db.session.add(Planet(name= "Jupiter", description="The largest planet, a gas giant with a Great Red Spot.", distance_from_sun="778.5")),
    db.session.add(Planet(name= "Saturn", description="Famous for its beautiful ring system.", distance_from_sun="1433.5")),
    db.session.add(Planet(name= "Uranus", description="An ice giant with a tilted axis.", distance_from_sun="2872.5")),
    db.session.add(Planet(name= "Neptune", description="A distant blue planet known for its strong winds.", distance_from_sun="4495.1")),
    db.session.commit()
    
    
    
    
    # class Planet:
#     def __init__(self, id, name, description, distance_from_sun):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.distance_from_sun = distance_from_sun
    
# planets = [
#     Planet(1, "Mercury", "The smallest and closest planet to the Sun", 57.9),
#     Planet(2, "Venus", "Similar in size to Earth, but with a toxic atmosphere.", 108.2),
#     Planet(3, "Earth", "Our home planet, the only known one with life.", 149.6),
#     Planet(4, "Mars", "The Red Planet, known for its dusty, rocky surface.", 227.9),
#     Planet(5, "Jupiter", "The largest planet, a gas giant with a Great Red Spot.", 778.5),
#     Planet(6, "Saturn", "Famous for its beautiful ring system.", 1433.5),
#     Planet(7, "Uranus", "An ice giant with a tilted axis.", 2872.5),
#     Planet(8, "Neptune", "A distant blue planet known for its strong winds.", 4495.1)
# ]