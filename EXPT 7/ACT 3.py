class Student:
    def __init__(self, name, marks_list):
        self.name = name
        self.marks_list = marks_list

    def calculate_percentage(self):
        total = sum(self.marks_list)
        percentage = total / len(self.marks_list)
        return percentage

    def calculate_grade(self):
        percentage = self.calculate_percentage()

        if percentage >= 90:
            grade = "A"
        elif percentage >= 75:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "Fail"

        print(f"\nStudent Name: {self.name}")
        print(f"Marks: {self.marks_list}")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Grade: {grade}")


# ---- User Input ----
name = input("Enter student name: ")
n = int(input("Enter number of subjects: "))

marks_list = []
for i in range(n):
    marks = float(input(f"Enter marks for subject {i+1}: "))
    marks_list.append(marks)

# Create object and display result
student1 = Student(name, marks_list)
student1.calculate_grade()
