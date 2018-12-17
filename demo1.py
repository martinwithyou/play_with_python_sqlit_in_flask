import time, threading

balance = 0
lock = threading.Lock()

def run_thread(n):
    for i in range(100000):

        lock.acquire()
        try:

            chang_it(n)
        finally:
            lock.release()


run_thread(500)