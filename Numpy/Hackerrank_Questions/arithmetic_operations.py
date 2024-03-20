'''Task

You are given two integer arrays,  and  of dimensions X.
Your task is to perform the following operations:

Add ( + )
Subtract ( - )
Multiply ( * )
Integer Division ( / )
Mod ( % )
Power ( ** )
Note
There is a method numpy.floor_divide() that works like numpy.divide() except it performs a floor division.

Input Format

The first line contains two space separated integers,  and .
The next  lines contains  space separated integers of array .
The following  lines contains  space separated integers of array .

Output Format

Print the result of each operation in the given order under Task.

Sample Input

1 4
1 2 3 4
5 6 7 8
Sample Output

[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]] '''


import numpy as np
r, c = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
m1= np.array(arr1).reshape(r, c)
m2= np.array(arr2).reshape(r, c)
addition = np.add(m1, m2)
substration = np.subtract(m1, m2)
multip = np.multiply(m1, m2)
div = np.floor_divide(m1, m2)
mod= np.mod(m1, m2)
power = np.power(m1,m2)
print(addition)
print(substration)
print(multip)
print(div)
print(mod)
print(power)