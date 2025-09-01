#program to show concept of class , instance and ineheritance
class Student:
    school_name = "ITM University"  
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display_info(self):
        print(f"Name: {self.name}, Roll No: {self.roll_no}, School: {self.school_name}")
student1 = Student("John Doe", 101)
student2 = Student("Jane Smith", 102)

student1.display_info()
student2.display_info()

student1.name = "Johnathan Doe"
student1.display_info()

Student.school_name = "New ITM University"
student1.display_info()
student2.display_info()

class GraduateStudent(Student):
    def __init__(self, name, roll_no, specialization):
        super().__init__(name, roll_no)
        self.specialization = specialization

    def display_info(self):
        super().display_info()
        print(f"Specialization: {self.specialization}")

        print(f"School: {self.school_name}")
        print(f"Graduate Student: {self.name}, Roll No: {self.roll_no}, Specialization: {self.specialization}")

grad_student = GraduateStudent("Alice Johnson", 201, "Computer Science")
grad_student.display_info()

"""
ALGORITHM:
1. Define a base Student class with class variable school_name and instance variables name, roll_no
2. Create methods for initialization and displaying student information
3. Create instances of Student class and demonstrate instance variable manipulation
4. Demonstrate class variable changes affecting all instances
5. Create GraduateStudent class inheriting from Student with additional specialization attribute
6. Override display_info method to show inheritance and method overriding

EXAMPLE OUTPUT:
Name: John Doe, Roll No: 101, School: ITM University
Name: Jane Smith, Roll No: 102, School: ITM University
Name: Johnathan Doe, Roll No: 101, School: ITM University
Name: Johnathan Doe, Roll No: 101, School: New ITM University
Name: Jane Smith, Roll No: 102, School: New ITM University
Name: Alice Johnson, Roll No: 201, School: New ITM University
Specialization: Computer Science
School: New ITM University
Graduate Student: Alice Johnson, Roll No: 201, Specialization: Computer Science
"""