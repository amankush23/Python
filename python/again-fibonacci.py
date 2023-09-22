# 6. Fibonacci Sequence:
# Write a program that generates and prints the first n terms of the Fibonacci sequence using a while loop.
n=int(input("enter the number:"))
a=0
b=1
print(a,b, end= ' ')
while n-2:
    c=a+b
    print(c, end=' ')
    a,b=b,c
    n-=1
   
