# app/models/user.py
from app.models.base import Base

class User(Base):
    def __init__(self, first_name, last_name):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"<User {self.first_name} {self.last_name}>"
