# app/models/place.py
from app.models.base import Base

class Place(Base):
    def __init__(self, name, description, location, user_id):
        super().__init__()
        self.name = name
        self.description = description
        self.location = location
        self.user_id = user_id  # Propietario (User)
        self.amenities = set()  # Conjunto para amenities para evitar duplicados
        self.reviews = []  # Lista para almacenar reseñas

    def add_amenity(self, amenity):
        """Agrega un amenity al conjunto de amenities."""
        self.amenities.add(amenity)

    def add_review(self, review):
        """Agrega una reseña a la lista de reseñas."""
        self.reviews.append(review)

    def __str__(self):
        return f"Place: {self.name}, Location: {self.location}"
