lst=[]
n=int(input("How many Elements ?:\n"))
for i in range(n):
    print("Enter list elements :")
    ele=int(input())
    lst.append(ele)
    sm=sum(lst)
    avg=sm/n
print("Maximum element is :",max(lst))
print("Minimum element is :",min(lst))
print("The Summitionof the Element is :",sum(lst))
print("Average of element is:",avg)