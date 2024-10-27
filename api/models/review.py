# app/models/review.py
from app.models.base import Base

class Review(Base):
    def __init__(self, content, rating, user_id, place_id):
        super().__init__()
        self.content = content
        self.rating = rating
        self.user_id = user_id  # User who wrote the review
        self.place_id = place_id  # Place being reviewed

    def __repr__(self):
        return f"<Review by User {self.user_id} for Place {self.place_id}>"
    