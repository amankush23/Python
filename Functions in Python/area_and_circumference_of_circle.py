def area(r):
    return 3.14*r**2
def crf(r):
    return 2*3.14*r

radius = int(input("enter the radius of the circle: "))
area = area(radius)
circumference = crf(radius)
print(f'The area of circle is: {area}')
print(f'The circumference of circle is: {circumference:.3f}')