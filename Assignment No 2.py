# Mohammad Uzer Qureshi::::::::::Assignment No 2::::::::::
n = int(input("Enter the numbers of inputs:\n"))
numbers = []
for i in range(n):
    num = int(input("Enter a number:\n "))
    numbers.append(num)

print("Maximum number:", max(numbers))
print("Minimum number:", min(numbers))
print("Summation:", sum(numbers))
print("Average:", sum(numbers)/n)
