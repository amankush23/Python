import threading
import time

def sun_calc(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)
t = threading.Thread(target=sun_calc, args=[5])
t.start()

