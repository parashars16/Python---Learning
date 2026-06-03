import math 
#circumference of circle
radius = float(input("Enter the radius of circle:"))
circumference = 2*math.pi*radius
print(f"The circumference is: {round(circumference, 2)}cm")

#area of circle 
radius = float(input("Enter the radius of circle:"))
area = math.pi*pow(radius , 2)
print(f"The area is {round(area, 2)}cm^2")