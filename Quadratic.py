import math
print("To solve quadratic equation")
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
print(f"Quadratic Equation: {a}^2x+{b}x+{c}")
r=b*b-4*a*c

if(r>0):
    r1=(-b+math.sqrt(r))/2*a
    r2=(-b-math.sqrt(r))/2*a
    print("Roots are ",r1,r2)
elif(r==0):
    r3=(-b)/2*a
    print("Root = ",r3)
else:
    print("Roots are not real")

    
