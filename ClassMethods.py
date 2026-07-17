class Students:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Students.count += 1
        Students.total_gpa += gpa

    def get_info(self):
        return f"{self.name} {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average GPA: {cls.total_gpa / cls.count:.2f}"


student1 = Students("Sheldon", 4.0)
student2 = Students("Penny", 2.0)
student3 = Students("Leonard", 3.5)

print(Students.get_count())
print(Students.get_average_gpa())