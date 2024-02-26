'''
 Code --> 1
 
 def apna(x):
    print(x)
x = map(apna, [3,10,34])
print(list(x))


 Code --> 2

def apna(x):
    return x
x = map(apna, [3,10,34])
print(list(x))

 Code --> 3

def apna_fun(x):
    return x
x = map(apna_fun,[3,10,42])
print(next(x))



class tmp:
    def __str__(self):
        return 'hello'
    def __repr__(self):
        return 'hi'

obj = tmp()
# if we will not type print then the 'hi' will be printed
#obj()
#if we will print the obj then the 'hello' will be printed
print(obj)

'''
ls = [3,4,5]
out = iter(ls)
print(next(out))