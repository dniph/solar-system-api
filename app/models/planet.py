from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import Optional
from ..db import db

from typing import TYPE_CHECKING
if TYPE_CHECKING: from .moon import Moon

class Planet(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)    
    name: Mapped[str] = mapped_column(nullable=True)
    description: Mapped[str]
    distance_from_sun:Mapped[float]
    moon_id: Mapped[Optional[int]] = mapped_column(ForeignKey("moon.id"))
    moon: Mapped[Optional["Moon"]] = relationship(back_populates="planets")
    
    def to_dict(self):
        planet_as_dict = {}
        planet_as_dict["id"] = self.id
        planet_as_dict["name"] = self.name
        planet_as_dict["description"] = self.description
        planet_as_dict["distance_from_sun"] = self.distance_from_sun

        return planet_as_dict    
    

    @classmethod
    def from_dict(cls, planet_data):
        new_planet = Planet(name=planet_data["name"],
                        description=planet_data["description"],
                        distance_from_sun=planet_data.get("distance_from_sun"))
        return new_planet
    












