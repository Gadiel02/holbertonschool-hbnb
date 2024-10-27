# app/models/base.py
from datetime import datetime
import uuid

class Base:
    def __init__(self):
        self.id = uuid.uuid4().hex  # Usa .hex para simplificar el ID
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """Updates the timestamp for the last modification."""
        self.updated_at = datetime.utcnow()

# app/models/user.py
from .base import Base

class User(Base):
    def __init__(self, first_name, last_name):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"User: {self.first_name} {self.last_name}"

# app/models/place.py
from .base import Base

class Place(Base):
    def __init__(self, name, description, location, user_id):
        super().__init__()
        self.name = name
        self.description = description
        self.location = location
        self.user_id = user_id
        self.amenities = set()  # Cambiado a set para evitar duplicados automáticamente
        self.reviews = []

    def add_amenity(self, amenity):
        """Add an amenity if it doesn't already exist."""
        self.amenities.add(amenity)

    def add_review(self, review):
        """Add a review to the place."""
        self.reviews.append(review)

    def __str__(self):
        return f"Place: {self.name}, Location: {self.location}"

# app/models/review.py
from .base import Base

class Review(Base):
    def __init__(self, content, rating, user_id, place_id):
        super().__init__()
        self.content = content
        self.rating = self.validate_rating(rating)
        self.user_id = user_id
        self.place_id = place_id

    @staticmethod
    def validate_rating(rating):
        """Validate that the rating is within the allowed range."""
        if 1 <= rating <= 5:
            return rating
        raise ValueError("Rating must be between 1 and 5.")

    def __str__(self):
        return f"Review by User {self.user_id} for Place {self.place_id} with Rating: {self.rating}"

# app/models/amenity.py
from .base import Base

class Amenity(Base):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return f"Amenity: {self.name}"

