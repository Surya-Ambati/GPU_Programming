
import psutil

print("Number of CPU cores:", psutil.cpu_count(logical=False))  # Physical cores
print("Number of logical CPU cores:", psutil.cpu_count(logical=True))  # Logical cores


import requests
import threading
from queue import Queue

urls = ["https://google.com", "https://youtube.com"]  # Can add more URLs

# Create a thread-safe queue and results list
url_queue = Queue()
results = []

# Worker function for threads
def download_worker():
    while True:
        url = url_queue.get()  # Get next URL from queue
        try:
            response = requests.get(url)
            results.append(len(response.text))
        except Exception as e:
            print(f"Error downloading {url}: {e}")
        finally:
            url_queue.task_done()  # Mark task as complete

# Create and start threads
num_threads = min(10, len(urls))  # Use 10 threads max
threads = []
for _ in range(num_threads):
    t = threading.Thread(target=download_worker)
    t.daemon = True  # Thread will exit when main program exits
    t.start()
    threads.append(t)

# Add all URLs to the queue
for url in urls:
    url_queue.put(url)

# Wait for all tasks to complete
url_queue.join()

print(f"Downloaded {len(results)} pages")
print(f"Results: {results}")



# CPU-bound example (prime checking)
from multiprocessing import Pool

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:  # ← Heavy computation here!
            return False
    return True

# Processes bypass Python's GIL to use all cores
with Pool(4) as p:  # Uses 4 CPU cores
    results = p.map(is_prime, [10**8+1, 10**8+3, 10**8+7])




'''
Processor: Physical chip doing the work. ex: Entire university infrastructure
Process: One active use of a program. ex: One active course session using that infrastructure

A progam is a set of instructions that a computer can execute. It is a collection of code and data that performs a specific task. A program can be written in various programming languages, such as Python, C++, Java, etc. A program can be executed by the operating system, which loads it into memory and runs it.

In memory, a program is divided into several segments, each of which has its own purpose. 
The main segments of a program are the code segment, data segment, heap segment, stack segment and registers.
The code segment contains the actual instructions that the CPU executes. It is read-only and cannot be modified during execution. The data segment contains global variables and static variables that are used by the program. The heap segment is used for dynamic memory allocation, where memory is allocated and deallocated at runtime. The stack segment is used for function calls and local variables, where memory is allocated and deallocated automatically when functions are called and return. Registers are small, fast storage locations in the CPU that are used to store data and instructions.

In addition to the segments, a program can also be divided into processes and threads.
A process is an instance of a program that is being executed. It has its own memory address space, and some common resources. A process can contain multiple threads, which are lightweight processes that share the same memory space as the main program. Threads are used for tasks that are I/O-bound or require frequent context switching.

Memory has cores, which are the physical units of processing in a computer. Each core can execute instructions independently, allowing for parallel processing. The number of cores in a CPU can vary, with some CPUs having multiple cores to handle multiple tasks simultaneously.
A program can be executed on a single core or multiple cores, depending on the design of the program and the capabilities of the CPU. In Python, the Global Interpreter Lock (GIL) limits the execution of threads to one at a time, but the multiprocessing module allows for parallel processing by creating separate processes that can run independently.


process: a process is simply an instance of a program that is being executed. It has its own shared memory address space, and some common resources. every process requires includes the code segment, data segment, heap segment, stack segment and registers. Processes are managed by the operating system and can run independently. 
In Python, the multiprocessing module allows you to create multiple processes to run tasks in parallel, bypassing the Global Interpreter Lock (GIL) and utilizing multiple CPU cores.

thread: a thread is a lightweight process that shares the same memory space as the main program. As other threads within the same process share the same memory space, they can communicate with each other more easily than processes. Threads are used for tasks that are I/O-bound or require frequent context switching.
Threads are managed by the operating system and can run concurrently. In Python, the threading module allows you to create multiple threads to run tasks concurrently, but they are limited by the GIL.

Stack: a stack is a data structure that stores data in a last-in, first-out (LIFO) manner. It is used to store function calls and local variables in a program. Each thread has its own stack, which is used to store local variables and function calls. The stack grows and shrinks as functions are called and return.
However, the stack size is limited, and if a thread uses too much stack space, it can cause a stack overflow. In Python, the default stack size is 8 MB on most platforms, but it can be changed using the sys.setrecursionlimit() function.

Heap: a heap is a data structure that stores data in a dynamic manner. It is used to store global variables and objects in a program. The heap is managed by the operating system and can grow and shrink as needed. In Python, the heap is used to store objects and data that are created at runtime. The heap size is limited by the amount of memory available on the system.
The heap is also used to store objects that are created using the new keyword in C++ or the malloc() function in C. In Python, the heap is managed by the garbage collector, which automatically frees memory that is no longer needed.

Registers: registers are small, fast storage locations in the CPU that are used to store data and instructions. They are used to store the current instruction being executed, the program counter, and other important information. Registers are much faster than RAM, but they are limited in size and number.
Registers are used to store data that is frequently accessed or modified, such as loop counters and function arguments. In Python, registers are not directly accessible, but they are used by the interpreter to optimize performance.

'''