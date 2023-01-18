# #Write a Program to Change a Given String where first and last Character have been Exchanged 
# str="Program"
# a=slice(str[0])
# b=slice(str[1:6])
# c=slice(str[-1])
# print(str[-1]+str[1:6]+str[0])
# def interchange_chr(str1):
#     return new_str[-1:]+
def fibonacci(n):
    a, b, c = 0, 1, 0
    for i in range(n):
        c = a + b
        print(c)
        a = b
        b = c

fibonacci(10)