import threading
import time

def exp(Timer):
    print("Timer started...")
    time.sleep(Timer)
    print("Timer Expired!!")

t = threading.Thread(target=exp, args=[4])
t.start()
