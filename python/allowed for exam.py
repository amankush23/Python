'''

A student will not be allowed to sit in exam if his attendence
is less than 75% take input from the user number of classed held and the attendence of the student.

'''
#input section
a=int(input("classes held:"))
b=int(input("classes attended:"))

#logic section
if a >= 0.75 * a :
    print("the student will be allowed")
else: 
   M=str(input("Did you give a medical certificate?"))
   if M=="Yes":
      print("allowed")
   else:
      print("not allowed")
