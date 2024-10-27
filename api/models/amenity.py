# app/models/amenity.py
from app.models.base import Base

class Amenity(Base):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __repr__(self):
        return f"<Amenity {self.name}>"
