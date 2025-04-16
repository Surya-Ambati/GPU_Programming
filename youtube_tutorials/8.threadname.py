import threading
import time

def myThread():
    print("Thread {} starting".format(threading.current_thread().getName()))
    time.sleep(10)
    print("Thread {} ending".format(threading.current_thread().getName()))

for i in range(4):
    threadName = "Thread-" + str(i)
    thread = threading.Thread(name=threadName, target=myThread)
    thread.start()
    print("{}".format(threading.enumerate()))