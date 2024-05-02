import threading
import random
import string
import time

def num_generator():
    n = 0
    while n<5:
        password = random.randint(1,100)
        print(password)
        time.sleep(1)
        n+=1

t = threading.Thread(target=num_generator)
t.start()