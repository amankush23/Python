'''Task

You are given a X integer array matrix with space separated elements ( = rows and  = columns).
Your task is to print the transpose and flatten results.

Input Format

The first line contains the space separated values of  and .
The next  lines contains the space separated elements of  columns.

Output Format

First, print the transpose array and then print the flatten.

Sample Input

2 2
1 2
3 4
Sample Output

[[1 3]
 [2 4]]
[1 2 3 4]'''

import numpy

def trans_flat(lst,m,n):
    arr = numpy.array(lst)
    trans_arr = arr.transpose()
    print(trans_arr)
    print(arr.flatten())
    

m,n = list(map(int,input().split()))
lst = []
for i in range(m):
    x=list(map(int,input().split()))
    lst.append(x)
trans_flat(lst,m,n)
