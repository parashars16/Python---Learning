class Company :
    class Employee:
     def __init__(self , name , position):
        self.name = name 
        self.positon = position

    def get__details(self):
       return f"{self.name}{self.positions}"
    
    def __init__(self , company_name):
       self.company_name = company_name
       self.employee = []

    def add__employee(self , name ,position):
       new__employee = self.employee(name , position)
       self.employees.append(new__employee)

    def list__employees(self):
       return [employee.get_detais() for employee in self.employees]

company1 = Company("IBM")
company2 = Company("Nagaro")

company1.add__employee("IronMan" , "Manager")
company1.add__employee("CaptainAmerica" ,"HR")
company1.add__employee("Hulk" , "Cashier")

company2.add__employee("Sheldon" , "Manager")
company2.add__employee("Penny" ,"Cashier")

for employee in company2.list__employees():
  print(employee)
   

