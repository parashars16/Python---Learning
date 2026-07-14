class Employees:

    def __init__(self ,name , position):
        self.name = name 
        self.position = position 

    def get__into(self):
        return f"{self.name} = {self.positon}"
    
    @staticmethod
    def is_valid_positon(position):
        valid_positons = ["Manager" , 'Cashier' , "Cook" , 'Janitor']
        return position in valid_positons
    

print(Employees.is_valid_positon("Rocket Scientist"))