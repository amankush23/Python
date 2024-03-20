'''Task

You are given a space separated list of numbers.
Your task is to print a reversed NumPy array with the element type float.

Input Format

A single line of input containing space separated numbers.

Output Format

Print the reverse NumPy array with type float.

Sample Input

1 2 3 4 -8 -10
Sample Output

[-10.  -8.   4.   3.   2.   1.]
'''
import numpy as np

# Input
x, y, z = map(int, input().split())
array_1 = np.array([input().split() for _ in range(x)], int)
array_2 = np.array([input().split() for _ in range(y)], int)

# Concatenating arrays along axis 0
concatenated_array = np.concatenate((array_1, array_2), axis=0)

# Output
print(concatenated_array)
