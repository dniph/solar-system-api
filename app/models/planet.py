from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)    
    name: Mapped[str]    
    description: Mapped[str]
    distance_from_sun:Mapped[float]
    
    @classmethod
    def from_dict(cls, planet_data):
        new_planet = Planet(name=planet_data["name"],
                        description=planet_data["description"],
                        distance_from_sun=planet_data.get("distance_from_sun"))
        return new_planet












