#MRO
class X:
    def disp(self):
        print("Display from X")
class A:
    def disp(self):
        print('Display from A')

class B(X):
    pass

class C(B,A):
    pass

obj = C()
obj.disp()
print(C.mro())

