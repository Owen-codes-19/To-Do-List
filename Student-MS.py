
# Student class
class Student:
    def __init__(self, name, age, studentId, grades):
        self.name = name
        self.age = age
        self.studentId = studentId
        self.grades = grades

# Sample students 
student_1 = Student("Owen", 20, 1, 100)
student_2 = Student("Denis", 5, 2, 90)
student_3 = Student("Ian", 4, 3, 50)

# Store all students in a list
students = []
students = [student_1, student_2, student_3]


# add students
def add_students():
    print("You have selected option 2. You can add data")
    name = (input("Enter the student's name: "))
    age = int(input("Enter the student's age: "))
    studentId = int(input("Enter the student's ID: "))    
    grades = int(input("Enter the student's grades: "))

    newStudent = Student(name, age, studentId, grades)
    students.append(newStudent)

    print(f"{name} has been added successfully!")


#  view students
def view_students():
    print("You have selected option 1. Here are the students:")

    for student in students:
        print(f"Name: {student.name}, Age: {student.age}, ID: {student.studentId}, Grade: {student.grades}")

# Main logic
while True:
    print("Welcome to the Student MS. You can save, add, and view student data. ")
    print("1 - View data")
    print("2 - Add data")
    print("3 - Save data")
    print("4 - Exit the program")

    user = input("Select a code to start: ")

    if user == "1":
        view_students()

    elif user == "2":
        add_students()

    elif user == "3":
        print("Coming soon!")

    elif user == "4":
        break
    
    else:
        print("Invalid choice.")