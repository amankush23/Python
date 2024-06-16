# n=int(input())

# if n//2!=0:
#     print("Weird")
# elif n//2==0 and 2<=n<=5:
#     print("Not Weird")
# elif n//2==0 and 6<=n<=20:
#     print("Weird")
# elif n%2==0 and n>20:
#     print("Not Weird")

# n=int(input())
# result = {
# n%2!=0:"Weird",
# n%2==0 and 2<=n<=5:"Not Weird",
# n%2==0 and 6<=n<=20:"Weird",
# n%2==0 and n>20:"Not Weird"
# }

# print(result[True])
num = eval(input("enter the number"))
flr = num//1
clr = -(-num//1)

print(f'{flr:.6f}')
print(f'{clr:.6f}')
