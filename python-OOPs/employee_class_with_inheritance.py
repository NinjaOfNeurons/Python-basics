class Employee:

    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary

    def show_details(self):             #abstraction no one  need to know what is show_deatils doing but it is doing something 
        print(
            "Employee name is",
            self.name,
            "and salary is:",
            self.salary                
        )


class Manager(Employee):

    def __init__(self, name: str, salary: int, department: str):      # encapsulated salary and other details by each department 
        super().__init__(name, salary)
        self.department = department

    
    def work(self):
        print("manager working time is 3-5")



class Devloper(Employee):

    def __init__(self, name: str, salary: int, department: str):   # encapsulated salary and other details
        super().__init__(name, salary)   #inheriting the class 
        self.department = department

    def work(self):                             #polymorphism can have diffrent diffrent class but with same name 
        print("devloper working time is 9-3")



manager = Manager("Karan", 80000, "AI")

manager.show_details()
print(manager.department)

emp = Employee("sad",5999)
emp.show_details()

manager.work()


dev = Devloper("sam", 3000000, 'security')
dev.work()