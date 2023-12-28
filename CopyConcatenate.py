print("To concatenate two strings\n")
def ConcatCopy(str1,str2):
    str3=a+b
    print("Concatenated String = ",str3,"\n")
    print("To copy two strings\n")
    
    cstr=""
    for i in str2:
        cstr=cstr+i
    print("String = ",str2)
    print(f"Copy of {str2} = ",cstr)

a=input("Enter first string: ")
b=input("Enter second string: ")
ConcatCopy(a,b)
