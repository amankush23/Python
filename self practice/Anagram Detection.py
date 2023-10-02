st1=input("enter the string1:")
st2=input("enter the string2:")

for i in st1:
    if i in st2:
        print("Yes it is anagram")
    else:
        print("No it is not anagram")