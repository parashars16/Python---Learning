class Animal:
    def __init__(self , name):
        self.name = name 
        self.isalive = True 

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is asleep")
    
class Dog(Animal):
     def speak(self):
         print("WOOF")

class Cat(Animal):
    def speak(self):
        print("SQUEEK")

dog = Dog("SCOOBY")
cat = Cat("GARFIELD")
