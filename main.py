class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        
class Person:
    def __init__(self, name, gender,is_driver):
        self.name = name
        self.gender = gender
        self.is_driver = is_driver
        self.hp = 100
        
leyla = Person("Leyla", "F", False)
john = Person("John", "M", True)
    
        