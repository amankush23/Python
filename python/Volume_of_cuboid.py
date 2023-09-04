#this program to find the volume and surface area of a cuboid, The length, width and height is entered by the user.

#input section
l=int(input("The length of cuboid:"))
b=int(input("The width of cuboid:"))
h=int(input("The height of cuboid:"))

#logic section
V=l*b*h
A=2*(l*b+b*h+h*l)

#display section
print("the volume of the cuboid is:",V,)
print("the surface area of cuboid is:",A)