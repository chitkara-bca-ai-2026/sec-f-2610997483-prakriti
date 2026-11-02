print("===============================================")
print("         CALENDER VERIFICATION SYSTEM          ")
print("===============================================")
year = int(input("Enter a year: "))
print()
status=""
days=""
days_feb=""
reason=""
print("---------------------------------------------------------------------------------")
if(year%4==0 and year%100!=0):
    status="LEAP YEAR"
    days="366"
    days_feb="29"
    reason="Divisible by 4 and not a century year"
elif(year%100 == 0):
    if(year%400 == 0):
            status="LEAP YEAR"
            days="366"
            days_feb="29"
            reason="Divisible by 400 and a century year"
    else:
            status="NOT A LEAP YEAR"
            days="365"
            days_feb="28"
            reason="Not divisible by 400 and a century year"
else:
        status="NOT A LEAP YEAR"
        days="365"
        days_feb="28"
        reason="Not divisible by 4 or a century year"
print(f"Year             : {year}")
print(f"STATUS           : {status}")
print(f"Days in Year     : {days}")
print(f"Days in February : {days_feb}")
print(f"Reason           : {reason}")
print("---------------------------------------------------------------------------------")