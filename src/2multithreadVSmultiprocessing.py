

'''
1. Concurrent Programming vs. Multithreading
Concept	Definition	Real-World Analogy	Example
Concurrent Programming	Doing multiple tasks apparently at the same time (may not be truly parallel)	A chef alternating between chopping veggies and stirring soup (one hand, but switches quickly)	A web server handling multiple requests "simultaneously"
Multithreading	A type of concurrency where a single process uses multiple threads	The chef now has two hands (threads) chopping and stirring truly at the same time	Running a Python script that downloads files while also processing data
Key Difference:

Concurrency is broader (includes threading, async, etc.).

Multithreading is one way to achieve concurrency.

2. Threading vs. Multiprocessing
Concept	Definition	Pros	Cons	Example
Threading	Multiple threads share the same memory in one process	Lightweight, fast communication	Risk of race conditions	Browser tabs (all tabs share browser memory)
Multiprocessing	Separate processes with independent memory	No memory conflicts, uses multiple CPU cores	Heavyweight, slower communication	Running Chrome + Photoshop separately
Key Differences:

Factor	Threading	Multiprocessing
Memory	Shared	Isolated
Safety	Risky (race conditions)	Safer
CPU Usage	Limited to one core	Uses all cores
Speed	Faster startup	Slower (new process)



When to Use What?
Concurrent Programming: Any task that waits (e.g., handling user input while downloading).

Threading: Multiple I/O tasks (e.g., serving web requests).

Multiprocessing: Heavy computations (e.g., video rendering).

Analogy:

Threading = Workers sharing one whiteboard (fast but messy).

Multiprocessing = Workers with their own whiteboards (organized but slower to share).'''


import threading

def task():
    print("Thread working")

# Create 2 threads
t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)
t1.start()  # Runs concurrently
t2.start()

# Use when: Tasks are I/O-bound (e.g., web scraping)


# Multiprocessing (Python)

import multiprocessing

def task():
    print("Process working")

# Create 2 processes
# if __name__ == '__main__':
#     p1 = multiprocessing.Process(target=task)
#     p2 = multiprocessing.Process(target=task)
#     p1.start()  # Runs in parallel
#     p2.start()

# Use when: Tasks are CPU-bound (e.g., math calculations).