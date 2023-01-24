# Assignment no: 4 Abrar Katri Rollno ::FB032
Number=int(input("Entre a Number : "))
reverse=0
while(Number>0): #jab tak input number 0 se bada hai yeh loop chalne doh 
    Remainder=Number%10
    reverse=(reverse*10)+Remainder
    Number=Number//10
    print(f"\nReverse of the Entered Number is {reverse}")