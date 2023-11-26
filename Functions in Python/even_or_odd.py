def even_or_odd(n):
    if n % 2 == 0:
        return "Even Number."
    else:
        return "Odd Number."
    
num=int(input("enter the number: "))
result=even_or_odd(num)
print(result)