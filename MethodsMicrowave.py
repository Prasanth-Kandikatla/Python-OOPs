# The attributes inside the initializer belongs to each object(instance) os the class (Microwave)
class Microwave:
    def __init__(self, brand: str, power_rating: str) -> None:
        self.brand = brand
        self.power_rating = power_rating
        self.turned_on: bool = False # Instance attribute, it belongs to each object

# We create 3 methods turn_on, turn_off and run inside the class 
# Such that all the class instances has access to these methods
# Here we use self to each attribute to specify that the attribute belongs to that particular instance
    def turn_on(self) -> None:
        if self.turned_on:
            print(f'Microwave "{self.brand}" is already Turned ON')
        else:
            self.turned_on = True
            print(f'Microwave "{self.brand}" is now Turned ON')

    def turn_off(self) -> None:
        if self.turned_on:
            self.turned_on = False
            print(f'Microwave "{self.brand}" is now Turned OFF')
        else :
            print(f'Microwave "{self.brand}" is already Turned OFF')

    def run(self, seconds: int) -> None:
        if self.turned_on:
            print(f'Running Microwave "{self.brand}" for {seconds} seconds')
        else :
            print(f'oops..! Turn on Microwave "{self.brand}"')


# Checking the methods functionality
smeg: Microwave = Microwave('smeg', 'B')
smeg.turn_on()
smeg.turn_off()
smeg.run(45)

bosch: Microwave = Microwave('bosch', 'C')
bosch.turn_on()
bosch.turn_on()
bosch.run(45)

