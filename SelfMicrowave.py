# "self" is the actual instance of the class
# It make sures that all the coming from the objects are sticking to the correct object (Instance)
# "self" is not a key word in python, we can use any name but "self" is the convention
class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating


smeg: Microwave = Microwave('smeg', 'B')
print(smeg.brand)
print(smeg.power_rating)

# As soon as we pass this information to the class
# the "self" is converted into "smeg" see the sample for understanding

    # def __init__(smeg, brand: str, power_rating: str) -> None:
    #     smeg.brand = brand
    #     smeg.power_rating = power_rating