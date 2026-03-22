#! Class
class Student:

    school_name = "ABC Public School"  # class attribute (shared)

    def __init__(self, name, roll, grade):
        self.name = name # instance attribute (per object)
        self.roll = roll # instance attribute (per object)
        self.grade = grade # instance attribute (per object)

    def display_info(self):
        print(f"Name: {self.name}, Roll: {self.roll}, Grade: {self.grade}")

    def update_grade(self, new_grade):
        self.grade = new_grade



s1 = Student("Ayesha", 101, "A")
s2 = Student("Amar", 102, "B")

s1.display_info()
s2.display_info()

s2.update_grade("A+")
s2.display_info()

print(s1.school_name)
print(s2.school_name)
