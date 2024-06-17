from EmployeesManager import EmployeeManager
class FrontendManager:

    def __init__(self):
        self.employee_manager = EmployeeManager()

    def print_menu(self):
        print('''Program Options:
                1) Add a new employee
                2) List all employees
                3) Delete by age range
                4) Update salary
                5) End the program''')
        
    def run(self):
        while True:
            self.print_menu()
            choice = int(input("Enter your choice (from 1 to 5): "))
            print()
            if choice>5 or choice<1 :
                print("Invalid range. Try again!\n")
            else:
                if choice == 1:
                    self.employee_manager.adding_new_employee()
                elif choice == 2:
                    self.employee_manager.employee_list()
                elif choice == 3:
                    self.employee_manager.delete_by_age()
                elif choice == 4:
                    self.employee_manager.update_salary()
                elif choice == 5:
                    print("Thank you!")
                    break


if __name__ == "__main__":
    frontend = FrontendManager()
    frontend.run()