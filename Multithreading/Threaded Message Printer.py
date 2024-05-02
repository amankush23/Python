import threading
import time

def message():
    while True:
        print("Hello World")
        time.sleep(2)
    
t = threading.Thread(target=message)
t.start()