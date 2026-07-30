from dataclasses import dataclass , field 

@dataclass 
class Person:
    name : str 
    age : int 
    password : str = field(repr = False)
    is_alive = bool = True 

    def __post__init__(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")

person1 = Person("Sheldon" , 30 , "pineapple")
person2 = Person("Amy" ,29 , "password")

print(person1)
print(person2)
print(person1 ==person2)
