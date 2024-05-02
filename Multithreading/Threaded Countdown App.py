import threading
import time
def reverse(x):
        for i in range(x, 0,-1):
            lst = []
            lst.append(i)
            print(i)
            time.sleep(1)

t = threading.Thread(target=reverse, args=[10])
t.start()


