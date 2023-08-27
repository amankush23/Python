#input section
p=int(input("enter the principal amount:"))
r=int(input("enter the rate:"))
n=int(input("number of times interest in compounded per year"))
t=int(input("enter the time:"))


#Logic section
A = p*(1+r/n)**(n*t)
out2= p+A

#display section
print("the compound interest is",A)
print("total amount is",out2)


