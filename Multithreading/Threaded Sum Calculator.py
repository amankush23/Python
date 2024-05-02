import threading
import time

def sun_calc():
    s = 0
    for i in range(1,101):
        s += i
    print("Sum of numbers from 1 to 100 is",s)
t = threading.Thread(target=sun_calc)
t.start()