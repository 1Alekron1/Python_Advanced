import requests
import time
from datetime import datetime
from threading import Thread, Lock
from queue import Queue

log_lock = Lock()
task_queue = Queue()

def fetch_timestamp_from_server(timestamp):
    response = requests.get(f"http://127.0.0.1:8080/timestamp/{timestamp}")
    if response.status_code == 200:
        return response.text
    else:
        return None

def write_log_entry(timestamp, date):
    log_line = f"{timestamp} {date}"
    with log_lock:
        with open("logs.txt", "a") as file:
            file.write(log_line + "\n")

def worker_thread():
    while True:
        timestamp = task_queue.get()
        if timestamp is None:
            break
        current_timestamp = time.time()
        date = fetch_timestamp_from_server(current_timestamp)
        if date is None:
            break
        write_log_entry(current_timestamp, date)
        time.sleep(1)
        task_queue.task_done()

if __name__ == "__main__":
    start_timestamp = int(time.time())
    threads = []
    for i in range(10):
        task_queue.put(start_timestamp + i)

    for _ in range(10):
        thread = Thread(target=worker_thread)
        thread.start()
        threads.append(thread)

    task_queue.join()

    for _ in range(10):
        task_queue.put(None)

    for thread in threads:
        thread.join()
