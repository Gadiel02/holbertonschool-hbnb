# app/services/facade.py
from app.repositories.in_memory_repository import InMemoryRepository
from app.models.user import User  # Import your models
# Repeat for other models as needed

class Facade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        # Initialize other repositories

    def add_user(self, user):
        self.user_repo.add(user)

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def all_users(self):
        return self.user_repo.all()

    def delete_user(self, user_id):
        self.user_repo.delete(user_id)

    def update_user(self, user):
        self.user_repo.update(user)
        