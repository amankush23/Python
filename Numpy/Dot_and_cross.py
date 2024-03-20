'''Task

You are given two arrays  and . Both have dimensions of X.
Your task is to compute their matrix product.

Input Format

The first line contains the integer .
The next  lines contains  space separated integers of array .
The following  lines contains  space separated integers of array .

Output Format

Print the matrix multiplication of  and .

Sample Input

2
1 2
3 4
1 2
3 4
Sample Output

[[ 7 10]
 [15 22]]'''

import numpy
n = int(input())
arr1 = [list(map(int, input().split())) for _ in range(n)]
arr2 = [list(map(int, input().split())) for _ in range(n)]
m1 = numpy.array(arr1)
m2 = numpy.array(arr2)
print(numpy.dot(m1, m2))