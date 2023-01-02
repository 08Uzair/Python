basic_Salary=int(input ("Enter your Basic Salary : \n"));
basic_Pay=int(input("Enter your basic pay : \n"));
if basic_Pay <0:
    print("Basic Pay cannot be negative ")
    exit()
elif basic_Salary <0:
    print("basic_Salarycannot be negative ")
    exit()
a=basic_Pay*0.1
b=basic_Pay*0.05
total_Salary=basic_Pay+a+b
c=total_Salary*0.02
d=total_Salary-c
print(f"The Salary which you get is {d}")