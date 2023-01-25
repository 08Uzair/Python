# Check Weather the given Sring is the Plaindrome or Not

str=input("Enter a String :\n ")
palin=str[::-1] #tO check wearher the given string is palindrome or not ::
if (list(str)==list(palin)):
    print("The Given String is the Palindrome")
else:
    print("The given String is not the Palindrome ")

# Check the given string is the Substring of the First String or Not

substr=input("Enter a Second String : \n")
if substr in str:
    print("The given String is the Substring of the First String")
else:
    print("The given string is not the substring of the First string")

# Check Weather the Give String 
str3=input("Enter Third String : \n")
if (list(str3)==list(str)):
    print("The First string is Equal to the Third String")
else:
    print("The First String is Not Equal to The Third String")