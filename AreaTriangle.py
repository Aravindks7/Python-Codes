import math

print("To find area of a triangle")
a=int(input("Enter side 1: "))
b=int(input("Enter side 2: "))
c=int(input("Enter side 3: "))

s=0
s=(a+b+c)/2
area=0

area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of triangle = ",area)
