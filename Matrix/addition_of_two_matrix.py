#matrix addition
class array:
    def __init__(self, lst):
        self.lst = lst
    def reshape(self, m, n):
        M = []
        tmp = []
        for i in self.lst:
            tmp.append(i)
            if len(tmp) == n:
                M.append(tmp)
                tmp = []
            self.lst = M
    def __add__(self, other):
        r = len(self.lst)
        c = len(self.lst[0])
        M = eval(str([[0]*c]*r))
        for i in range(r):
            for j in range(c):
                M[i][j]=self.lst[i][j] + other.lst[i][j]
        return array(M)
        M=[]
        self.lst
        other.lst
        return array(M)
    def dis(self):
        for i in self.lst:
            print(*i)

    # def dot(self,other):
    #     r1 = len(self.lst)
    #     c1 = len(self.lst[0])
    #     r2 = len(other.lst)
    #     c2 = len(other.lst[0])
    #     M = eval(str([[0] * c2] * r1))
    #     for i in range(r1):
    #         for j in range(c2):
    #             for k in range(c1):
    #                 M[i][j] += self.lst[i][k] *other.lst[k][j]
    #     return array(M)
    # def transpose(self):
    #     pass




#raw array
lst1 = list(map(int,input().split()))
r1,c1 = list(map(int,input().split()))
arr1 = array(lst1)
arr1.reshape(r1,c1)
print('\nMatrix1')
arr1.dis()
lst2 = list(map(int,input().split()))
r2,c2 = list(map(int,input().split()))
arr2 = array(lst2)
arr2.reshape(r2,c2)
print('\nMatrix2')
arr2.dis()

if (r1,c1) == (r2,c2):
    print('\nAddition')
    addition = arr1 + arr2
    addition.dis()
else:
    print("Invalid!")

# multiply = arr1 * arr2
# multiply.dis()



