print("To check given string is palindrome or not")
str=input("Enter a String: ")

estr=""
for i in str:
    estr=i+estr

if(str==estr):
    print(f"{str} is a palindrome")
else:
    print(f"{str} is not a palindrome")
    
