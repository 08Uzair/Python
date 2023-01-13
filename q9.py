a=("1","2","3","4")
b=("a","b","c","d")
for i in a:
    for j in b:
        print(i,j, end=" ")

for i in range (1,11):
    print(i, end="  ")
else:
    print ("out of the loop")


for i in range (1,11):
    print(f"Multiplication of table {i}")
    for j in range (1,11):
        print(f"{i}X{j}={i*j}")


mydict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(mydict)

a="""red
green
blue"""
print(a)