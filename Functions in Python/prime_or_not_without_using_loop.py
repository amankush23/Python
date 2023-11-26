#To check whether the given number is prime or not without using loop.
def prime_or_not(n):
    return ["not a prime number" for i in range(2,n) if n % i == 0 ]
num=int(input("enter the number: "))
prime=prime_or_not(num)
print(prime)

    
