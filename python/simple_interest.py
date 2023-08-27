#input section
p=int(input("enter the principal amount:"))
r=int(input("enter the rate:"))
t=int(input("enter the time:"))

#Logic section
out1=(p*r*t)/100
out2= p+out1

#display section
print("the simple interest of principle amount is",out1)
print("total amount is",out2)
