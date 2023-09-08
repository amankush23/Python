'''

Given an integer number and two divisors d1 and d2, we have to check whether number is divisible by d1 and d2 or not.


'''

number = int(input())
d1 = int(input())
d2 = int(input())


if number % d1 == 0 and number % d2 == 0:
    print("Yes.")
else:
    print("No.")
