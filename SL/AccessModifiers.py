class Car:
    def __init__(self, carprice, carmodel, carcolor):
        self.__price = carprice
        self._model = carmodel
        self.color = carcolor

    # Defining Mutator Method
    def set_price(self, carprice):
        self.__price = carprice

    def set_model(self, carmodel):
        self._model = carmodel

    def set_color(self, carcolor):
        self.color = carcolor

    # Defining Accessor Method
    def get_price(self):
        return self.__price

    def get_model(self):
        return self._model

    def get_color(self):
        return self.color

# Creating an object
myCar = Car(10000, 'Ford', 'Red');

print (myCar.get_model())
print (myCar.get_price())
print (myCar.get_color())

myCar.set_model('Porche')
myCar.set_price(20000)
myCar.set_color('Blue')

print (myCar.get_model())
print (myCar.get_price())
print (myCar.get_color())

print(myCar.__price)  # This will raise an AttributeError since __price  is private
print(myCar._model)  # This will print 'Porche' since _model is protected and can be accessed outside the class
print(myCar.color)  # This will print 'Blue' since color is public and can be accessed outside the class