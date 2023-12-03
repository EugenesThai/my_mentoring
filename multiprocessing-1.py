from multiprocessing import Process, freeze_support
from time import sleep


def worker(task_id):
    print(f"Staring task with id {task_id}")
    sleep(2)
    print(f"Finishing task with id {task_id}")


if __name__ == "__main__":
    freeze_support()

    processes = []

    for i in range(1, 5):
        p = Process(target=worker, args=(i,))
        processes.append(p)

    for p in processes:
        p.start()

    for process in processes:
        process.join()

    print("My worker has finished!")
