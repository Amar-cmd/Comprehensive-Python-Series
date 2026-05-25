# Employee Payroll System (Beginner Friendly, Console Based)
# OOP: Abstraction (ABC) + Polymorphism
# Menu: match-case (Python 3.10+)

from abc import ABC, abstractmethod


# -------------------- Abstract Class --------------------
class Employee(ABC):
    def __init__(self, emp_id: str, name: str):
        self.emp_id = emp_id
        self.name = name

    @abstractmethod
    def calculate_salary(self) -> float:
        pass

    def display_details(self) -> None:
        print(f"[{self.emp_id}] {self.name} ({self.__class__.__name__})")

    def generate_payslip(self) -> None:
        salary = self.calculate_salary()
        print("\n--- PAYSLIP ---")
        print("Name :", self.name)
        print("ID   :", self.emp_id)
        print("Role :", self.__class__.__name__)
        print("Salary:", salary)
        print("-" * 25)


# -------------------- Employee Types --------------------
class Manager(Employee):
    def __init__(self, emp_id: str, name: str, basic: float, bonus: float, allowance: float):
        super().__init__(emp_id, name)
        self.basic = basic
        self.bonus = bonus
        self.allowance = allowance

    def calculate_salary(self) -> float:
        return self.basic + self.bonus + self.allowance


class Intern(Employee):
    def __init__(self, emp_id: str, name: str, stipend: float, months: int):
        super().__init__(emp_id, name)
        self.stipend = stipend
        self.months = months

    def calculate_salary(self) -> float:
        return self.stipend * self.months


class FullTimeEmployee(Employee):
    def __init__(self, emp_id: str, name: str, basic: float, hra: float):
        super().__init__(emp_id, name)
        self.basic = basic
        self.hra = hra

    def calculate_salary(self) -> float:
        # Simple version: no PF/Tax to keep it beginner friendly
        return self.basic + self.hra


# -------------------- Payroll System --------------------
class PayrollSystem:
    def __init__(self):
        self.employees = {}  # emp_id -> employee object

    def add_employee(self, emp: Employee) -> None:
        if emp.emp_id in self.employees:
            print("Employee ID already exists.")
            return
        self.employees[emp.emp_id] = emp
        print("Employee added.")

    def remove_employee(self, emp_id: str) -> None:
        if emp_id not in self.employees:
            print("Employee not found.")
            return
        del self.employees[emp_id]
        print("Employee removed.")

    def display_all_employees(self) -> None:
        if not self.employees:
            print("No employees.")
            return
        print("\nAll Employees:")
        for emp in self.employees.values():
            emp.display_details()

    def print_payslip(self, emp_id: str) -> None:
        emp = self.employees.get(emp_id)
        if not emp:
            print("Employee not found.")
            return
        emp.generate_payslip()

    def total_payroll(self) -> float:
        # Polymorphism: calculate_salary() works for all types
        total = 0.0
        for emp in self.employees.values():
            total += emp.calculate_salary()
        return total


# -------------------- Helpers --------------------
def read_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("Enter a valid number.")


def read_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Enter a valid amount.")


# -------------------- Main Program --------------------
ps = PayrollSystem()

while True:
    print("\n--- Employee Payroll System ---")
    print("1. Add Manager")
    print("2. Add Intern")
    print("3. Add FullTime Employee")
    print("4. Remove Employee")
    print("5. Display All Employees")
    print("6. Print Payslip")
    print("7. Total Payroll")
    print("8. Exit")

    choice = read_int("Enter choice: ")

    match choice:
        case 1:
            emp_id = input("Employee ID: ").strip()
            name = input("Name: ").strip()
            basic = read_float("Basic Salary: ")
            bonus = read_float("Bonus: ")
            allowance = read_float("Allowance: ")
            ps.add_employee(Manager(emp_id, name, basic, bonus, allowance))

        case 2:
            emp_id = input("Employee ID: ").strip()
            name = input("Name: ").strip()
            stipend = read_float("Stipend per month: ")
            months = read_int("Months: ")
            ps.add_employee(Intern(emp_id, name, stipend, months))

        case 3:
            emp_id = input("Employee ID: ").strip()
            name = input("Name: ").strip()
            basic = read_float("Basic Salary: ")
            hra = read_float("HRA: ")
            ps.add_employee(FullTimeEmployee(emp_id, name, basic, hra))

        case 4:
            emp_id = input("Employee ID to remove: ").strip()
            ps.remove_employee(emp_id)

        case 5:
            ps.display_all_employees()

        case 6:
            emp_id = input("Employee ID for payslip: ").strip()
            ps.print_payslip(emp_id)

        case 7:
            print("Total Payroll:", ps.total_payroll())

        case 8:
            print("Bye!")
            break

        case _:
            print("Invalid choice.")
