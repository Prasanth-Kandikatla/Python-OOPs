# We use __init__ is a constructor (dunder method)
# It runs automatically when you create an object
# It returns none by default
# __init__ is the initializer 
# __init__ initializes the attributes of newly created objects(smeg, bosch)
# We can have only one initializer inside a class
class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating


# We should pass the exact number of arguments to initialize the object
smeg: Microwave = Microwave('smeg', 'B')
print(smeg.brand)
print(smeg.power_rating)

bosch: Microwave = Microwave()
print(bosch.brand)
print(bosch.power_rating)

