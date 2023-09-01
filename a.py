#write a program that converts a given number of days into weeks and days.
#input section

a=int(input("enter the number of days: "))

#logic section
out1=a//7
out2=a%7

#display section
print("the weeks are",out1,"and the days are",out2)



