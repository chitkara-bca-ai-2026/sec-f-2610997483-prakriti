name = input("Enter employee name: ")
name  = str(name)
print(type(name))
employee_id = input("Enter employee I'd: ")
employee_id = int(employee_id)
print(type(employee_id))
salary = input("Enter your salary: ")
salary = float(salary)
print(type(salary))
department = input("Enter your department: ")
department = str(department)
print(type(department))
active = input("Is the employee active? (Yes/No): ")
if active == "Yes" or active == "yes" or active == "YES":
    active = True
elif active == "No" or active == "no" or active == "NO":
    active = False
print(type(active))
print("------ EMPLOYEE DETAILS ------")
print(f" Name      : {name}")
print(f" ID        : {employee_id}")
print(f" Salary    : {salary}")
print(f" Department: {department}")
print(f" Active    : {active}")