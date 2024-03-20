'''You are given the coefficients of a polynomial .
Your task is to find the value of  at point .

Input Format

The first line contains the space separated value of the coefficients in .
The second line contains the value of .

Output Format

Print the desired value.

Sample Input

1.1 2 3
0
Sample Output

3.0'''

import numpy as np

# Taking input
coefficients = list(map(float, input().split()))
x = float(input())

# Evaluating polynomial at the given point
result = np.polyval(coefficients, x)

# Printing the result
print(result)