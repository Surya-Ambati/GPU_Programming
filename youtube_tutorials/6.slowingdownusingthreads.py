import time
import random
import threading

def calculatePrimeFactors(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac

def executeProc():
    for i in range(1000):
        rand = random.randint(20000, 100000000)
        print(calculatePrimeFactors(rand))

def main():
    print("Starting number crunching")
    t0 = time.time()
    threads = []
    for i in range(10):
        thread = threading.Thread(target=executeProc)
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    t1 = time.time()
    totalTime = t1 - t0
    print("Execution Time: {}".format(totalTime))

if __name__ == '__main__':
    main()



'''
Explanation in Simple Terms
What’s Happening?
The calculatePrimeFactors(n) function finds the prime factors of a number (e.g., for 12, it returns [2, 2, 3]).
The executeProc() function runs this calculation 1000 times on random numbers between 20,000 and 100,000,000.
In main(), we create 10 threads, each running executeProc(), and measure how long it takes for all threads to finish.
We compare the performance of three approaches:
Single-threaded: One thread does all the work (3.69 seconds).
Multiprocessing: 10 processes (1.98 seconds).
Multithreaded: 10 threads (3.95 seconds).
Why Threads Slowed Down the Program:
The GIL (Global Interpreter Lock): In Python, the GIL ensures that only one thread can execute Python bytecode at a time, even on a multi-core CPU. This means threads don’t run in parallel for CPU-intensive tasks like prime factorization—they take turns.
Overhead of Threads: Creating and managing threads adds overhead (like scheduling them to take turns). With 10 threads, they’re all fighting to use the same CPU core, which creates delays.
Comparison:
Single-threaded (3.69 seconds): No thread overhead, just one worker doing the job.
Multiprocessing (1.98 seconds): Processes run on separate cores (true parallelism), so the work is split efficiently.
Multithreaded (3.95 seconds): Threads take turns on one core, plus the overhead of managing 10 threads makes it slower than even the single-threaded version.
Analogy: Imagine 10 chefs (threads) trying to bake cakes in one kitchen (a single process with the GIL). They have to take turns using the oven (CPU core), which slows them down. Meanwhile, 10 chefs in 10 separate kitchens (processes) can bake at the same time on different ovens (cores), finishing faster.
Key Point: For CPU-intensive tasks (like calculations), threads in Python can slow things down due to the GIL. Use multiprocessing instead to take advantage of multiple cores. Threads are better for I/O-bound tasks (e.g., downloading files), where they can wait without holding the GIL.

'''