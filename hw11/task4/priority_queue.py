import threading
import time
from queue import PriorityQueue


class Producer(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        print("Producer: Running")
        tasks = self._generate_tasks()
        self._put_tasks(tasks)
        print("Producer: Done")

    def _generate_tasks(self):
        return [
            (0, "Task(priority=0)."),
            (2, "Task(priority=2)."),
            (1, "Task(priority=1)."),
            (4, "Task(priority=4)."),
            (3, "Task(priority=3)."),
            (6, "Task(priority=6)."),
        ]

    def _put_tasks(self, tasks):
        for priority, task in tasks:
            self.queue.put((priority, task))
            time.sleep(0.5)


class Consumer(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        print("Consumer: Running")
        self._consume_tasks()
        print("Consumer: Done")

    def _consume_tasks(self):
        while True:
            priority, task = self.queue.get()
            if task is None:
                self.queue.task_done()
                break
            self._process_task(priority, task)
            self.queue.task_done()

    def _process_task(self, priority, task):
        print(f">{task}          sleep({priority * 0.1})")
        time.sleep(priority * 0.1)


def main():
    queue = PriorityQueue()
    producer = Producer(queue)
    consumer = Consumer(queue)

    producer.start()
    consumer.start()

    producer.join()
    queue.put((None, None))
    queue.join()
    consumer.join()


if __name__ == "__main__":
    main()
