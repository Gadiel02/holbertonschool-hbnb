# app/repositories/place_repository.py
class PlaceRepository:
    def __init__(self):
        self.places = {}

    def add(self, place):
        self.places[place.id] = place

    def all(self):
        return list(self.places.values())

    def get(self, place_id):
        return self.places.get(place_id)

    def update(self, place):
        self.places[place.id] = place
