class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}"

# Example usage:
student1 = Student("Ali", 20, "S123")
print(student1.display_info())
