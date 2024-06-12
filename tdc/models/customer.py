# customer.py
import uuid

class Customer:
    def __init__(self, name, age, nickname, cellphone):
        self.id = str(uuid.uuid4())
        self.name = name
        self.age = age
        self.nickname = nickname
        self.cellphone = cellphone

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "nickname": self.nickname,
            "cellphone": self.cellphone
        }
