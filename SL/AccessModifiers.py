class Car:
    def __init__(self, carprice, carmodel, carcolor):
        self._price = carprice
        self._model = carmodel
        self.color = carcolor

    # Defining Mutator Method
    def set_price(self, carprice):
        self._price = carprice

    def set_model(self, carmodel):
        self._model = carmodel

    def set_color(self, carcolor):
        self.color = carcolor

    # Defining Accessor Method
    def get_price(self):
        return self._price

    def get_model(self):
        return self._model

    def get_color(self):
        return self.color

# Creating an object
MyBMW = Car(10000, 'BMW', 'Red');

print (MyBMW.get_model())
print (MyBMW.get_price())
print (MyBMW.get_color())

MyBMW.set_model('Porche')
MyBMW.set_price(20000)
MyBMW.set_color('Blue')

print (MyBMW.get_model())
print (MyBMW.get_price())
print (MyBMW.get_color())

#print(MyBMW.__price)  # This will raise an AttributeError since __price  is private
print(MyBMW._model)  # This will print 'Porche' since _model is protected and can be accessed outside the class
print(MyBMW.color)  # This will print 'Blue' since color is public and can be accessed outside the class