from models import ToDoModel

class ToDoService:
    def __init__(self):
        self.model = ToDoModel()

    def create(self, params):
        #print("abc")
        print(params)
        return self.model.create(params)

    def delete(self, item_id):
        return self.model.delete(item_id)

    def update(self, item_id, params):
        print(params)
        return self.model.update(item_id, params)

    def list_all(self):
        return self.model.list_items()
