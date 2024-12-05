# Parent Class: Student
class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")

    def study(self):
        print(f"{self.name} is studying.")

# Child Class: GraduateStudent
class GraduateStudent(Student):
    def __init__(self, name, age, student_id, thesis_title):
        super().__init__(name, age, student_id)  # Inherit from Student class
        self.thesis_title = thesis_title

    def study(self):
        super().study()  # Call the parent class study method
        print(f"{self.name} is researching for thesis: {self.thesis_title}")

    def defend_thesis(self):
        print(f"{self.name} is defending their thesis titled '{self.thesis_title}'.")

# Child Class: UndergraduateStudent
class UndergraduateStudent(Student):
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age, student_id)  # Inherit from Student class
        self.major = major

    def study(self):
        super().study()  # Call the parent class study method
        print(f"{self.name} is studying {self.major}.")

    def join_club(self, club_name):
        print(f"{self.name} joined the {club_name} club.")

# Creating objects of the classes

# Parent class object
student = Student("John Doe", 20, "S12345")
student.display()
student.study()

# Graduate student object
grad_student = GraduateStudent("Alice Smith", 25, "G98765", "Machine Learning in Healthcare")
grad_student.display()
grad_student.study()
grad_student.defend_thesis()

# Undergraduate student object
undergrad_student = UndergraduateStudent("Bob Johnson", 19, "U54321", "Computer Science")
undergrad_student.display()
undergrad_student.study()
undergrad_student.join_club("Robotics")
