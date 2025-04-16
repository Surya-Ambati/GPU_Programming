import threading
import time

def threadTarget():
    print("Current Thread: {}".format(threading.current_thread()))

threads = []
for i in range(10):
    thread = threading.Thread(target=threadTarget)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()


'''
Starting Multiple Threads:
You can create and start many threads using a loop, but they run independently, so their order isn’t predictable.
Use threading.enumerate() to see all active threads at any moment.

Threads Can Slow Down CPU-Intensive Tasks:
For tasks like calculations (CPU-bound), threads in Python don’t run in parallel due to the GIL—they take turns, which can make things slower.
Use multiprocessing for CPU-bound tasks to run on separate cores and speed things up.
Threads are better for I/O-bound tasks (e.g., waiting for a file or network response), where the GIL doesn’t slow things down.

Monitoring Threads:
Use threading.active_count() to check how many threads are currently running.
Use threading.current_thread() to identify which thread is executing a piece of code.

Why This Matters
Managing Threads: Knowing how to start and monitor threads helps you handle multiple tasks in your program, like downloading files or processing data.
Performance: Understanding the GIL’s impact helps you choose between threads (for I/O tasks) and processes (for CPU tasks) to avoid slowing down your program.
Debugging: Tools like threading.active_count() and threading.current_thread() make it easier to debug multithreaded programs by showing you what’s happening.

'''