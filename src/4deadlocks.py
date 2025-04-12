import threading
import time



'''
A deadlock in Python (or in any programming context) is a situation in multithreaded or multiprocess programming where two or more threads or processes are unable to proceed because each is waiting for the other to release a resource, resulting in a standstill. 
In Python, deadlocks typically occur when using threading (with locks, semaphores, or other synchronization primitives) or multiprocessing, as Python’s Global Interpreter Lock (GIL) can complicate thread behavior, though the GIL itself does not directly cause deadlocks.

What is a Deadlock?
A deadlock occurs when the following four conditions (known as the Coffman conditions) are met simultaneously:

Mutual Exclusion: At least one resource must be held in a non-shareable mode (e.g., a lock that only one thread can hold at a time).
Hold and Wait: A thread holding at least one resource is waiting to acquire another resource that is currently held by another thread.
No Preemption: Resources cannot be forcibly taken away from a thread; the thread must release them voluntarily.
Circular Wait: A set of threads form a circular chain where each thread is waiting for a resource that the next thread in the chain holds.
In Python, deadlocks often arise when using threading.Lock, threading.RLock, or other synchronization primitives improperly.

'''


# Create two locks - these will be used to create a deadlock scenario.
lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1_function():
    print("Thread 1: Acquiring lock1")
    with lock1:
        time.sleep(1)  # Simulate some work
        print("Thread 1: Acquiring lock2")
        with lock2:
            print("Thread 1: Both locks acquired")

def thread2_function():
    print("Thread 2: Acquiring lock2")
    with lock2:
        time.sleep(1)  # Simulate some work
        print("Thread 2: Acquiring lock1")
        with lock1:
            print("Thread 2: Both locks acquired")

# Create two threads
thread1 = threading.Thread(target=thread1_function)
thread2 = threading.Thread(target=thread2_function)

# Start the threads
thread1.start()
thread2.start()

# Wait for the threads to finish (this will never happen due to deadlock)
thread1.join()
thread2.join()

print("Main thread finished")

