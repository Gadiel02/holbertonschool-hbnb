# app/repositories/in_memory_repository.py
class InMemoryRepository:
    def __init__(self):
        self.data = {}

    def add(self, item):
        self.data[item.id] = item

    def get(self, item_id):
        return self.data.get(item_id)

    def all(self):
        return list(self.data.values())

    def delete(self, item_id):
        if item_id in self.data:
            del self.data[item_id]

    def update(self, item):
        self.data[item.id] = item
