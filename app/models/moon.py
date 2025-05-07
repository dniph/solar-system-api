from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from typing import Optional

from typing import TYPE_CHECKING
if TYPE_CHECKING: from .planet import Planet

class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    planets: Mapped[list["Planet"]] = relationship(back_populates="moon")

    def to_dict(self):
        moon_as_dict = {
            "id": self.id,
            "name": self.name
        }
        
        return moon_as_dict
    
    @classmethod
    def from_dict(cls, moon_data):
        new_moon = cls(name=moon_data["name"])
        return new_moon