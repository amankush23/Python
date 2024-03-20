'''Task

You are given two integer arrays of size X and X ( &  are rows, and  is the column). Your task is to concatenate the arrays along axis .

Input Format

The first line contains space separated integers ,  and .
The next  lines contains the space separated elements of the  columns.
After that, the next  lines contains the space separated elements of the  columns.

Output Format

Print the concatenated array of size X.

Sample Input

4 3 2
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 
Sample Output

[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] '''

import numpy as np

# Input
x, y, z = map(int, input().split())
array_1 = np.array([input().split() for _ in range(x)], int)
array_2 = np.array([input().split() for _ in range(y)], int)

# Concatenating arrays along axis 0
concatenated_array = np.concatenate((array_1, array_2), axis=0)

# Output
print(concatenated_array)
