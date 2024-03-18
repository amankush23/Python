class Matrix:
    def __init__(self, arr):
        self.arr = arr
    def validity(self, m, n):
        return len(self.arr) == m*n
    def create_matrix(self, m, n):
        self.m = []
        for i in range(m):
            self.m.append(self.arr[i*n:i*n+n])

    def dis(self):
        for i in self.m:
            print(*i)

lst = list(map(int,input().split()))
row, column = list(map(int, input().split()))
m  = Matrix(lst)
#print (m.validity (row, column))
if m.validity(row, column):
    m.create_matrix(row, column)
    m.dis()
else:
    print('Invalid Dimensions')