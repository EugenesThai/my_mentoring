import time
import threading

lock = threading.Lock()

counter = 0
threads = []


def add_counter():
    global counter
    with lock:
        for _ in range(100):
            counter += 1


def thr_example():
    for i in range(1, 4):
        t = threading.Thread(target=add_counter)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()


thr_example()
print(counter)
