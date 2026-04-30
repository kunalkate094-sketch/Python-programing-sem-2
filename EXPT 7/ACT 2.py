class Employee:
    def __init__(self, name, basic_salary):
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self, bonus):
        if bonus < 0:
            print("Invalid bonus amount")
        else:
            total_salary = self.basic_salary + bonus
            print(f"Employee Name: {self.name}")
            print(f"Basic Salary: ₹{self.basic_salary}")
            print(f"Bonus: ₹{bonus}")
            print(f"Total Salary: ₹{total_salary}")

# Call the class
emp1 = Employee("Kunal", 20000)
emp1.calculate_salary(5000)
