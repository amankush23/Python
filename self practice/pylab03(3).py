# Invalid Parentheses

st=input()
count=0

for i in st:
    if i == '(':
         count+=1
    else:
        count-=1
        if count<0:
            break
print("'True'" if count ==0 else "'False'")