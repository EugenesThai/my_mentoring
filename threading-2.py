from concurrent.futures import ThreadPoolExecutor, wait


def worker(task_id):
    print(f"Task with id {task_id} done")


def main():
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(worker, task_id) for task_id in range(1, 5)]
        wait(futures)


main()

# В чём разница между concurrent.futures.wait() и pool.shutdown(wait=True)?
