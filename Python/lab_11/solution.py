name = input("Enter Username: ")
password = input("Enter Password: ")
x = False
if len(password)>=8:
    x = True
else:
    pass
count = 0
flag=0
for i in range(0,len(password)-1):
    if password[i].isupper:
        count+=1
    else:
        pass
    if password[i].isdigit:
        flag+=1
    else:
        pass
if x==True and count>=1 and flag>=1:
    print("Valid Password")
else:
    print("Invalid Password")