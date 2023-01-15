def recure_fibo(n):
    if n<=1:
        return n
    else:
       return(recure_fibo(n-1))+recure_fibo(n-2) 
       #take the input from the user
nterms=int(input("How Many terms:\n"))
#check if the number is valid or not
if nterms<=0:
    print("Please Entre a Positive Integer")
    for i in range (nterms):
        print(recure_fibo(i))
