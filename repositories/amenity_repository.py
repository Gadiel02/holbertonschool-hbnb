# app/repositories/amenity_repository.py
class AmenityRepository:
    def __init__(self):
        self.amenities = {}

    def add(self, amenity):
        self.amenities[amenity.id] = amenity

    def all(self):
        return list(self.amenities.values())

    def get(self, amenity_id):
        return self.amenities.get(amenity_id)

    def update(self, amenity):
        self.amenities[amenity.id] = amenity
