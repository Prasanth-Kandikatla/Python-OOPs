# Dunder Methods also called as Magic Methods
# Actual name is double underscore methods
class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False

# When we add two instances using "+" operator, python looks only for __add__ method
# We can have anyoperation inside the __add__ method (not strictky addition)
# It is convention for better readability and understanding if the code
# If we want fusion of two instances we can use the __add__ dunder method
    def __add__(self, other) -> str:
        return (f'{self.brand} + {other.brand}') 
        
    def __mul__(self, other) -> str:
        return (f'{self.brand} * {other.brand}') 
    
# str method is used for understanding purpose of non developers
    def __str__(self) -> str:
        return (f'{self.brand}, Rating: {self.power_rating}')
    
# repr is used for developers understanding (Contains more specific data)
    def __repr__(self)-> str:
        return f'Microwave: "{self.brand}", power_rating: "{self.power_rating}"'

# Creating instances
bosch: Microwave = Microwave('bosch', 'C')
sam: Microwave = Microwave('sam', 'C')

# By default "print(bosch)" calls __str__ method
print(bosch)

# We have to explicitly specify "print(repr(bosch))" to call the __repr__ method
print(repr(bosch))
