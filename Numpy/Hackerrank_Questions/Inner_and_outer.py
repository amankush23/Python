'''Task

You are given two arrays:  and .
Your task is to compute their inner and outer product.

Input Format

The first line contains the space separated elements of array .
The second line contains the space separated elements of array .

Output Format

First, print the inner product.
Second, print the outer product.

Sample Input

0 1
2 3
Sample Output

3
[[0 0]
 [2 3]]'''

import numpy
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
m1 = numpy.array(arr1)
m2 = numpy.array(arr2)
i = numpy.inner(m1,m2)
o = numpy.outer(m1,m2)
print(i)
print(o)