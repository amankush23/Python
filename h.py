import math
#input section 
a=int(input("enter the first side:"))
b=int(input("enter the second side:"))
c=int(input("enter the third side:"))

#logic section
s=(a+b+c)/2
A=math.sqrt(s*(s-a)*(s-b)*(s-c))

#display section
print("the area of triangle is",A)