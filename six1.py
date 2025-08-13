# section 13 :  Serializers

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return f'{self.name} is {self.age} years old.'