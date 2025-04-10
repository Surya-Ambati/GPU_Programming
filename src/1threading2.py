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

