def area(a,b):
    return a*b
def perimeter(a,b):
    return 2*(a+b)

#main code
a=int(input("enter the length of rectangle: "))
b=int(input("enter the breadth of rectangle: "))
area=area(a,b)
perimeter=perimeter(a,b)
print(f'the area of rectangle is: {area} ')
print(f'the perimeter of rectangle is: {perimeter} ')