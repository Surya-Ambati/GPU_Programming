
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