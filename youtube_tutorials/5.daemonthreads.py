import threading
import time

def standardThread():
    print("Starting my Standard Thread")
    time.sleep(20)
    print("Ending my standard thread")

def daemonThread():
    while True:
        print("Sending Out Heartbeat Signal")
        time.sleep(2)

if __name__ == '__main__':
    standardThread = threading.Thread(target=standardThread)
    daemonThread = threading.Thread(target=daemonThread)
    daemonThread.setDaemon(True)
    daemonThread.start()
    standardThread.start()

'''
Note: when we flag a thread as a daemon, it means that the thread will run in the background and will not prevent the program from exiting.
When the main program exits, all daemon threads are killed. This is useful for background tasks that should not block the program from terminating.

Daemon threads are typically used for tasks like monitoring, logging, or performing periodic actions without blocking the main program.
Daemon threads are not suitable for tasks that require cleanup or finalization, as they may be abruptly terminated when the program exits.
Daemon threads are not guaranteed to finish their work before the program exits, so they should be used with caution.


'''