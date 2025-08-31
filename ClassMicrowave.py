# Creating Microwave class
# We follow Camel case while defining a class name by convention
class Microwave:
    pass

# "smeg" is the class instance which means it is a unique Microwave 
#  It will have its own characteristics along with the class characteristics
# ": Microwave" this part below is convention(Type hint). Part of good documentation
smeg: Microwave = Microwave()
print(smeg) # <__main__.Microwave object at 0x00E25328>