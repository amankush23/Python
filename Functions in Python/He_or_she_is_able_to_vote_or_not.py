def vote(age):
    if age>=18:
        return "Can Vote"
    else:
        return "Cannot Vote"

a=int(input("enter the age of him/her: "))
v=vote(a)
print(v)