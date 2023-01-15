#Mohammad Uzer Qureshi:::::Assignment No 3:::::
lst=[]   # Number of Subject's as input 
n=int(input("Enter Number of Subjects :\n"))  # iterating till the range
for i in range(0,n):
    sub=int(input("Entre Marks of Subjects:\n"))
    if(sub<40):
        print("Grade:Fail")
        exit()
    lst.append(sub)  # adding the elements
    print(lst)
avg=sum(lst)/5
if (avg>=75):
    print("Grade: A+")
elif(avg>=60 and avg<75):
    print("Grade: A")
elif(avg>=50 and avg<60):
    print("Grade: B")
elif(avg>=40 and avg<50):
    print("Grade: C")
else:
    print("Grade:Fail")
