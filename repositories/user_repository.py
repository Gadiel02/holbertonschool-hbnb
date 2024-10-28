# app/repositories/user_repository.py
class UserRepository:
    def __init__(self):
        self.users = {}

    def add(self, user):
        self.users[user.id] = user

    def all(self):
        return list(self.users.values())

    def get(self, user_id):
        return self.users.get(user_id)

    def update(self, user):
        self.users[user.id] = user
        