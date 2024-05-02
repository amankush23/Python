import threading
import time
def fun1():
    for i in range(1, 11):
        print(i)
        time.sleep(5)
def fun2():
    for i in range(65, 91):
        print(chr(i))
        time.sleep(.8)

T1 = threading.Thread(target=fun1)
T2 = threading.Thread(target=fun2)
T1.start()
T2.start()
