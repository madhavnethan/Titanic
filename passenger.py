class Passenger:
    def __init__(self, name, gender, age):
        self.name = name
        self.age = age
        self.gender = gender
    
    def __str__(self):
        return f"{self.name}, {self.age}, {self.gender}"
        
