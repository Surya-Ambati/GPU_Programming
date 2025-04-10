# # Example: Assign processes to specific cores (CPU affinity)
# import os
# import multiprocessing as mp

# def worker():
#     print(f"Running on core {os.getpid() % 2}")

# if __name__ == "__main__":
#     processes = [mp.Process(target=worker) for _ in range(2)]
#     [p.start() for p in processes]
#     [p.join() for p in processes]


# actual core used (CPU affinity)
# Example: Assign processes to specific cores (CPU affinity)

import psutil
import multiprocessing as mp
import threading

# def worker(core_id):
#     p = psutil.Process()
#     p.cpu_affinity([core_id])  # Works on Windows/Linux/Mac
#     print(f"Running on core {core_id}")

# if __name__ == "__main__":
#     processes = [
#         mp.Process(target=worker, args=(i % 2,))
#         for i in range(2)
#     ]
#     [p.start() for p in processes]
#     [p.join() for p in processes]




# Example: Using threading with synchronization primitives


def worker(lock, thread_id):
    with lock:  # Only one thread runs this block at a time
        print(f"Thread {thread_id} is working")

if __name__ == "__main__":
    lock = threading.Lock()
    threads = [threading.Thread(target=worker, args=(lock, i)) for i in range(8)]
    [t.start() for t in threads]  # Starts all threads
    [t.join() for t in threads]   # Waits for completion



'''
Donkeys (Cores):

Use multiprocessing for true parallelism.

Assign CPU affinity to optimize core usage.


Chickens (Threads):

Use threading + synchronization primitives (Lock, Semaphore).

Partition resources (e.g., separate queues for different tasks).


Avoid Contention:

For CPU-bound work: Split data across cores.

For I/O-bound work: Use async (asyncio) or thread pools.


Real-world:

Web servers (chickens = requests, scratch = connection pools).

GPU programming (donkeys = CUDA cores, chickens = warps).


'''