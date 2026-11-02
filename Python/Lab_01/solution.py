print("Welcome to the Student fee calculator")
print("Please enter the details according to the per semester")
tution_fee = int(input("Enter the tuition fee: "))
lab_fee = int(input("Enter the lab fee : "))
library_fee = int(input("Enter the library fee : "))
exam_fee= int(input("Enter the exam fee : "))
sem =float(tution_fee + lab_fee + library_fee + exam_fee )
choice = (input("choose is your discount in percentage or in airthmatic \nPress 1 if discount is in percentage and 2 if it is in airthmatic : "))
dis = float(input("Now enter your discount : "))
total_sem = float(0.0)
if choice == "1":
    total_sem =  sem - ((dis/100)*(sem))
elif choice == "2":
    total_sem = sem - dis
total_year_fee = float(total_sem * 2)
year = int(input("Enter your course duration in year : "))
total_month = year * 12
total_fee = float(total_year_fee*year)
monthly_expence = total_fee / total_month
print("Your monthly expence would be : ", monthly_expence)