def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function
a=int(input("enter the number:"))
result = factorial(a)
print(f"The factorial of {a} is {result}")
