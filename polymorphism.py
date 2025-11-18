# built-in polymorphism

print(len("hello")) # works on string and returns 5

print(len([1 , 2, 3])) # works on list and returns 3


# method overriding(runtime polymorphism)

class Animal:
    def speak(self):
        return "some sound"
    

class Dog(Animal):
    def speak(self):
        return "bark"


class Cat(Animal):
    def speak(self):
        return "meow"


Animals = [Dog(), Cat(), Animal()] 
for a in Animals:
    print(a.speak())      


# method overloading (compile-time polymorphism)     

class Calculator:
    def add(self, a = 0, b = 0, c = 0):
        return a + b + c
    
calc = Calculator()
print(calc.add(2, 3)) # returns 5
print(calc.add(2, 3, 4)) # returns 9
print(calc.add()) # returns 0


class Vehicle:
    def fuel_type(self):
        return "type"
    
class Car(Vehicle):
    def fuel_type(self):
        return "petrol"  


class Bike(Vehicle):
    def fuel_type(self):
        return "electric"
    

class Truck(Vehicle):
    def fuel_type(self):
        return "diesel"




Vehicles = [Car(), Bike(), Truck()]
for a in Vehicles:
    print(a.fuel_type())