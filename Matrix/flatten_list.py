#nested list
lst = [2, [[[10]]], [1,3],[], [1,[0]]]
#output(flatten list)
for i in lst:
    a =[]
    if type(i) == []:
        lst = str(i).replace('[','')
        out = lst.replace(']','')
        print(list(eval(out)))
    
        a.extend(i)
print(a)
# lst = str([i for i in lst if i]).replace('[','')
# out = lst.replace(']','')
# print(list(eval(out)))