import json
import os

class Student:
    def __init__(self, student_id, name, age, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.marks = marks

    def calculate_average(self):
        total = sum(self.marks)
        return total / len(self.marks)

    def get_grade(self):
        average = self.calculate_average()

        if average >= 90:
            return "A"
        elif average >= 75:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 40:
            return "D"
        else:
            return "Fail"

    def display(self):
        print("\nStudent Details")
        print("--------------------")
        print("ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)
        print("Average:", self.calculate_average())
        print("Grade:", self.get_grade())


class StudentManagement:

    def __init__(self):
        self.students = []
        self.filename = "students.json"

    def add_student(self):
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        age = int(input("Enter Student Age: "))

        marks = []

        for i in range(5):
            mark = int(input(f"Enter subject {i+1} marks: "))
            marks.append(mark)

        student = Student(student_id, name, age, marks)
        self.students.append(student)

        print("Student added successfully!")

    def view_students(self):
        if len(self.students) == 0:
            print("No students found!")
            return

        for student in self.students:
            student.display()

    def search_student(self):
        student_id = int(input("Enter Student ID to search: "))

        for student in self.students:
            if student.student_id == student_id:
                student.display()
                return

        print("Student not found!")

    def delete_student(self):
        student_id = int(input("Enter Student ID to delete: "))

        for student in self.students:
            if student.student_id = student_id:
                self.students.remove(student)
                print("Student deleted successfully!")
                return

        print("Student not found!")

    def save_data(self):
        data = []

        for student in self.students:
            data.append({
                "id": student.student_id,
                "name": student.name,
                "age": student.age,
                "marks": student.marks
            })

        with open(self.filename, "w") as file:
            json.dump(data, file)

        print("Data saved successfully!")

    def load_data(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

            for item in data:
                student = Student(
                    item["id"],
                    item["name"],
                    item["age"],
                    item["marks"]
                )
                self.students.append(student)

        except FileNotFoundError:
            print("File not found!")


def main():

    system = StudentManagement()

    while True:

        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Save Data")
        print("6. Load Data")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            system.add_student()

        elif choice == 2:
            system.view_students()

        elif choice == 3:
            system.search_student()

        elif choice == 4:
            system.delete_student()

        elif choice == 5:
            system.save_data()

        elif choice == 6:
            system.load_data()

        elif choice == 7:
            print("Exiting program...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()