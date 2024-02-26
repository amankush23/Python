def add(a,b):
    return a +b
def deco(fun):
    def wraper(a,b):
        print("This is Addition Program")
        return fun(a,b)
    return wraper
# re = deco(add)
# out = re(3,4)
# out = add(2,5)
# print(out)
re = deco(add)(3,4)
print(re)