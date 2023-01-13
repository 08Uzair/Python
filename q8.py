start=int(input("Entre a start number :\n"))
end=int(input("Entre a ending number :\n"))
for i in range (start,end+1):
    flag=0
    for j in range(2,i):
        if i%j==0:
            flag=1
    if (flag==1):
        print(i,end='  ')