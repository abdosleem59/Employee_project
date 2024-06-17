from Employee import Employee
    
class EmployeeManager:
    def __init__(self):
        self.emp_list=[]

    def adding_new_employee(self):
        print("Enter employee data: ")
        name = input("Enter the name: ")
        age = int(input("Enter the age: "))
        salary = float(input("Enter the salary: "))
        print()
        new_employee = Employee(name, age, salary)
        self.emp_list.append(new_employee)
        


    def employee_list(self):
        print("**Employee List**")
        for emp in self.emp_list:
            print(f'Employee: {emp.name} has age {emp.age} and salary {emp.salary}\n')

    
    def delete_by_age(self):
        start_age = int(input("Enter age from: "))
        end_age = int(input("Enter age to: "))
        print()
        for idx, emp in enumerate(self.emp_list):
            if end_age>= emp.age >= start_age:
                self.emp_list.pop(idx)

    
    def update_salary(self):
        name = input("Enter name: ")
        new_salary = float(input("Enter new salary: "))
        print()
        found = False
        for emp in self.emp_list:
            if emp.name == name:
                found = True
                emp.salary = new_salary
        if found==False:
            print("Error: No employee with such a name\n")
            
