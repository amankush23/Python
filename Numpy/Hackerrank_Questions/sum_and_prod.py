'''Task

You are given a 2-D array with dimensions X.
Your task is to perform the  tool over axis  and then find the  of that result.

Input Format

The first line of input contains space separated values of  and .
The next  lines contains  space separated integers.

Output Format

Compute the sum along axis . Then, print the product of that sum.

Sample Input

2 2
1 2
3 4
Sample Output

24'''

import numpy
m,n = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(m)]
lst = numpy.array(arr)
s = numpy.sum(lst, axis = 0)
p = numpy.prod(s)
print(p)