'''You are given a square matrix  with dimensions X. Your task is to find the determinant. Note: Round the answer to 2 places after the decimal.

Input Format

The first line contains the integer .
The next  lines contains the  space separated elements of array .

Output Format

Print the determinant of .

Sample Input

2
1.1 1.1
1.1 1.1
Sample Output

0.0'''

import numpy as np

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(float, input().split())))

det = np.linalg.det(arr)
print(round(det, 2))
