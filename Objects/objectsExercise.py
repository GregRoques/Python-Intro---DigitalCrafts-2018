# # a class is a recipe
# # an object is the food you made with the recipe
# # the recipe ca be used lots, and lots of times

# # Our blueprint for making cars is called "Car"
# class Car(object):
#     # whenever we start making a new car, __init__ will run
#     # we ALWAYS pass self first
#     def __init__(self):
#         # self refers to THIS object
#         self.make = "Honda"
#         self.model = "Accord"
#         self.year = "2007"

# myCar = Car()

# yourCar = Car()
# yourCar.make = "Toyota"

# print yourCar.make
# print myCar.make

# # _____________________________________________________________

# myCar2 = {
#     "make": "Honda",
#     "model": "Accord",
#     "year": "2007"
# }

# print myCar2["make"]

# # _____________________________________________________________

class Car(object):
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def changeModel =(self, newModel)
        self.model = newModel

zachsCar = Car("Toyota", "Carolla")
print zachsCar.model

zachsCar.isCool = "Awesome"
print zachsCar.isCool

zachsCar.changeModel("Fiesta")