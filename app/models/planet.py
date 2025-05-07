from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)    
    name: Mapped[str] = mapped_column(nullable=True)
    description: Mapped[str]
    distance_from_sun:Mapped[float]
    
    @classmethod
    def from_dict(cls, planet_data):
        new_planet = Planet(name=planet_data["name"],
                        description=planet_data["description"],
                        distance_from_sun=planet_data.get("distance_from_sun"))
        return new_planet
    
    def to_dict(self):
        planet_as_dict = {}
        planet_as_dict["id"] = self.id
        planet_as_dict["name"] = self.name
        planet_as_dict["description"] = self.description
        planet_as_dict["distance_from_sun"] = self.distance_from_sun

        return planet_as_dict












