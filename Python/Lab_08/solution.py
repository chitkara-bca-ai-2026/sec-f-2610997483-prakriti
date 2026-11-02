name = input("Enter your name: ")
roll_no = int(input("Enter your roll no: "))
total = 0
fail = False
i = 1
marks = 0
while i<=5:
    marks = int(input(f"Enter your marks in {i} subject : "))
    if marks>=0 and marks<=100:
        if marks < 40:
            fail = True
        elif marks>=40:
            total = total + marks
    else:
        print("Please enter valid marks")
        break
    i+=1
per = (total/500)*100
if fail == True:
    print(f"Result = Fail \nGrade= F \nRemarks =  Failed in one or more subjects")
elif fail == False:
    if per>=90:
        print("Grade = A \nRemarks = Outstanding")
    elif per>=80:
        print("Grade = B \nRemarks = Excellent")
    elif per>=60:
        print("Grade = C \nRemarks = Good")
    elif per>=50:
        print("Grade = E \nRemarks = Marginal Pass")