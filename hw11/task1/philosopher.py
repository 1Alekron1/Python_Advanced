import logging
import threading
import random
import time
from typing import List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Philosopher(threading.Thread):
    is_running = True

    def __init__(self, left_fork: threading.Lock, right_fork: threading.Lock) -> None:
        super().__init__()
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self) -> None:
        while self.is_running:
            logger.info(f"Philosopher {self.name} starts thinking.")
            time.sleep(random.randint(1, 10))
            logger.info(f"Philosopher {self.name} is hungry.")
            with self.left_fork, self.right_fork:
                logger.info(f"Philosopher {self.name} acquired forks.")
                self.dine()

    def dine(self) -> None:
        logger.info(f"Philosopher {self.name} starts eating.")
        time.sleep(random.randint(1, 10))
        logger.info(
            f"Philosopher {self.name} finishes eating and goes back to thinking."
        )


def main() -> None:
    forks: List[threading.Lock] = [threading.Lock() for _ in range(5)]
    philosophers: List[Philosopher] = [
        Philosopher(forks[i % 5], forks[(i + 1) % 5]) for i in range(5)
    ]
    Philosopher.is_running = True
    for philosopher in philosophers:
        philosopher.start()
    time.sleep(200)
    Philosopher.is_running = False
    logger.info("Program finished.")


if __name__ == "__main__":
    main()
