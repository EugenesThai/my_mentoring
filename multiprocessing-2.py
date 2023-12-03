from multiprocessing import Process, Pool, freeze_support
from time import sleep


def worker(task_id):
    print(f"Staring task with id {task_id}")
    sleep(2)
    print(f"Finishing task with id {task_id}")


if __name__ == "__main__":
    tasks = [x for x in range(1, 5)]

    with Pool(processes=len(tasks)) as pool:
        pool.map(worker, tasks)

    print("My worker has finished!")

# СЛОЖНААА!!!
