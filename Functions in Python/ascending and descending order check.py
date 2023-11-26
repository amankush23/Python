#write a python program to check the list of integers is ascending order or descending order.

def sorted_or_not(lst):
    temp=lst.copy()
    temp.sort()
    if temp == lst:
        return 1
    elif temp == lst[::-1]:
        return 0
    else:
        return -1

lst=[3,5,1,0,7,9]
result=sorted_or_not(lst)
print(result)
