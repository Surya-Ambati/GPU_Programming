'''
GPU Programming Connection:

CPU threads → Few heavy workers

GPU threads → Thousands of lightweight workers

Same principles, different scale!

'''

from threading import Thread, current_thread
import threading
import time, os

start = time.time()
print("Starting...")

def run_in_park(number):
    print(f"Thread {current_thread().name} is running in the park")
    print(f"current thread id: {current_thread().ident}")
    print(f"Completed round {number} in the park")
    time.sleep(2)  # Simulate time taken to run in the park

def swim_in_pool(number):
    print(f"Thread {current_thread().name} is swimming in the pool")
    print(f"current thread id: {current_thread().ident}") # current_thread().ident is the thread id
    print(f"Completed lap {number} in the pool")
    time.sleep(3)  # Simulate time taken to swim in the pool

# Launch 4 parallel threads
threads = []
for i in range(4):
    t1 = threading.Thread(target=run_in_park, args=(i,)) #we can also use kwargs, list of args. ex: kwargs={'number': i} . Note, for tuple args must pass as (i,)
    threads.append(t1)
    t1.start()
    

for j in range(4):
    t2 = threading.Thread(target=swim_in_pool, args=(j,))
    threads.append(t2)
    t2.start()

for t in threads:
    t.join()
    print(f"Thread {t.name} has finished execution")
    print(f"Thread {t.name} is alive: {t.is_alive()}") # check if thread is alive or not. It will be false after join() is called.
    print(f"Thread {t.name} is daemon: {t.daemon}") # check if thread is daemon or not. It will be false after join() is called.
    # print(f"Thread {t.name} is main thread: {t.is_main_thread()}") # check if thread is main thread or not. It will be false after join() is called.
    print(f"Thread {t.name} identity id: {t.ident}") # check the thread id. 
    print(f"Thread {t.name} native id: {t.native_id}") # check the thread is alive or not. It will be false after join() is called.
    
print("All threads completed")
end = time.time()
print(f"Time taken: {end - start:.2f} seconds")
print(os.getpid()) # get the process id of the current process. It will be same for all threads.

