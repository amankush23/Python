''' task is, you will be given 2 integers and a thershold k. 
find the maximum value between bitwise and, or and xor. the maximum should not greater than the thershold k.
default maximum value is zero.'''

a,b =input().split()
a=int(a)
b=int(b)
k=int(input())

re1=a&b
re2=a|b
re3=a^b

re1=re1*(re1<k)
re2=re1*(re2<k)
re3=re3*(re3<k)

print(max(re1,re2,re3))