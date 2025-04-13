import multiprocessing
import os

def child():
    print("We are in the child process with PID= %d" % os.getpid())

def parent():
    print("We are in the parent process with PID= %d" % os.getpid())
    # Create a new process
    process = multiprocessing.Process(target=child)
    process.start()
    print("We are in the parent process and our child process has PID= %d" % process.pid)
    process.join()  # Wait for the child process to finish

if __name__ == '__main__':
    parent()


'''
Note:
Forking vs. Multiprocessing:
Forking (with os.fork()) creates a new process that’s an exact copy of the parent, sharing memory until changes are made (copy-on-write). 
It’s a low-level UNIX/LINUX feature.

multiprocessing provides a higher-level interface for process creation and communication, abstracting away platform differences. 
On Windows, it doesn’t use forking but achieves the same goal (a new process).


•	Forking means creating a new process by cloning the current one (a specific way to do multiprocessing, mostly on UNIX systems).
•	Multiprocessing is the general idea of running multiple processes, and it can use forking (on UNIX) or spawning (on Windows).
•	Separate Cores: Yes, forking or multiprocessing creates processes that can run on separate cores, allowing true parallelism. Threads in Python, however, take turns on one core due to the GIL (unless they’re doing I/O tasks).


PID: Process ID, a unique identifier for each process in the system.
Parent Process: The original process that creates child processes.
Child Process: A new process created by a parent process. It can execute concurrently with the parent and other child processes.

'''