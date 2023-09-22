n=int(input("ENTER THE AMMOUNT:"))

if n>=25000:
    print("customer will get into Gold category","and","amount to be paid.",n-(n*0.5))
elif 10000<=n   and n<25000:
    print("customer will get into silver category","and","amount to be paid.",n-(n*0.1))
else:
    print("customer will get into BRONZE category","and","amount to be paid.",n-(n*0.05))
