import threading
import time

def char_printer(x= "Hello"):
    for i in x:
        print(i)
        time.sleep(1)
t = threading.Thread(target=char_printer)
t.start()
