#Mohammad Uzair Qureshi:::::::::Assignment no 1::::
basic_pay=int(input("Entre your Basic Pay :\n"))
basic_pay=float(basic_pay)
if basic_pay<0 : #Basic Pay Cannot be Zero
    print("Basic Pay Can't be Negative")
    exit()
hra=basic_pay*0.1   #hra is 16% of Basic Pay
ta=basic_pay*0.05   #ta is 5% of Basic Pay
total_salary=basic_pay+hra+ta
professional_tax=total_salary*0.02   #Profesional tax is 2% of Toral Salary
salary_payable=total_salary*professional_tax
print(f"Salary Payable is {salary_payable}")
