from threading import Thread, current_thread, active_count, enumerate, get_native_id
import threading

def hello_world():
    for i in range(5):
        print("Hello World!")
        print(f"Thread Name: {current_thread().name}")
        print(f"Thread ID: {current_thread().ident}")


def hello_universe():
    for i in range(4):
        print("Hello Universe!")
        print(f"Thread Name: {current_thread().name}")
        print(f"Thread ID: {current_thread().ident}")


t1 = Thread(target=hello_world, name="World Thread")
print(t1.is_alive()) # check if thread is alive or not. It will be false after join() is called.
t1.start()
print(f"active_count() = {active_count()}") # check the number of active threads. It will be 1 after join() is called.
print(f"current_thread() = {current_thread().name}") # check the current thread name. It will be main thread after join() is called.
print(enumerate()) # check the list of active threads. It will be empty after join() is called
print(" --> main thread id: ", get_native_id()) # check the native id of the current thread. It will be same for all threads.
print(t1.is_alive())

# t2 = Thread(target=hello_universe, name="Universe Thread")
# print(t2.is_alive()) # check if thread is alive or not. It will be false after join() is called.
# t2.start()
# print(f"active_count() = {active_count()}") # check the number of active threads. It will be 1 after join() is called.
# print(f"current_thread() = {current_thread().name}") # check the current thread name. It will be main thread after join() is called.
# print(t1.is_alive())


print("Waiting for threads to finish...")
t1.join() # wait for thread to finish, suppose if we remove t1.join(), it will continue run mainthread and print below statements.

print("---Thread 1 has finished execution---")
print(f"Thread 1 is alive: {t1.is_alive()}") # check if thread is alive or not. It will be false after join() is called.
print(f"Thread 1 is daemon: {t1.daemon}") # check if thread is daemon or not. It will be false after join() is called.


# Racing Condition:

'''
When one or more threads are trying to access the same resource at the same time, it is called racing condition.
This can lead to unexpected results and bugs in the program. To avoid this, we can use locks or semaphores to synchronize the access to the shared resource.

To handle the racing condition, we can use the threading module's Lock class. A lock is a synchronization primitive that can be used to protect shared resources from being accessed by multiple threads at the same time.
A lock can be acquired by a thread and released when the thread is done with the shared resource. This ensures that only one thread can access the shared resource at a time, preventing racing conditions.

There are three types of locks in Python:
1. Lock: A simple lock that can be acquired and released by a thread.
2. RLock: A reentrant lock that can be acquired multiple times by the same thread. This is useful when a thread needs to acquire a lock multiple times before releasing it.
3. Semaphore: A lock that allows a fixed number of threads to acquire it at the same time. This is useful when we want to limit the number of threads that can access a shared resource at the same time.

'''

'''
Execptions occured in threads:
1. Unhandled exceptions in threads can cause the program to crash or behave unexpectedly.
2. To handle exceptions in threads, we can use the try-except block inside the thread's target function.
3. We can also use the threading module's Thread class's setDaemon() method to set the thread as a daemon thread. A daemon thread is a thread that runs in the background and does not block the program from exiting.
4. Daemon threads are terminated when the main thread exits, so they should not be used for tasks that need to be completed before the program exits.
5. To handle exceptions in daemon threads, we can use the try-except block inside the thread's target function and log the exception to a file or print it to the console.
6. We can also use the threading module's Thread class's join() method to wait for the thread to finish before exiting the program.
7. This ensures that all threads have completed their tasks before the program exits.
8. We can also use the threading module's Thread class's is_alive() method to check if a thread is still running or not.
9. This can be useful for debugging and monitoring the status of threads in the program.
10. We can also use the threading module's Thread class's name attribute to give a name to the thread. This can be useful for debugging and monitoring the status of threads in the program.
'''

'''
What happens when exceptions occur in threads? 
will it terminate the main thread or not? also will it impact other threads or not?

1. If an exception occurs in a thread, it will not terminate the main thread or other threads.
2. The main thread will continue to run and other threads will also continue to run.    
3. However, if the exception is not handled properly, it may cause the thread to terminate and not complete its task.




'''