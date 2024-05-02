import logging
import random
import threading
import time
from typing import List

TOTAL_TICKETS: int = 10

logging.basicConfig(level=logging.INFO)
logger: logging.Logger = logging.getLogger(__name__)


class Seller(threading.Thread):
    def __init__(self, semaphore: threading.Semaphore, cv: threading.Condition) -> None:
        super().__init__()
        self.sem: threading.Semaphore = semaphore
        self.cv: threading.Condition = cv
        self.tickets_sold: int = 0
        logger.info("Seller started work")

    def run(self) -> None:
        global TOTAL_TICKETS
        while True:
            self._work()
            with self.sem:
                if TOTAL_TICKETS <= 0:
                    break
                self._sell_ticket()
                self._notify_director_if_needed()

    def _work(self) -> None:
        self._random_sleep()

    def _sell_ticket(self) -> None:
        global TOTAL_TICKETS
        self.tickets_sold += 1
        TOTAL_TICKETS -= 1
        logger.info(f"{self.name} sold one; {TOTAL_TICKETS} left")

    def _notify_director_if_needed(self) -> None:
        global TOTAL_TICKETS
        if TOTAL_TICKETS <= 1:
            with self.cv:
                self.cv.notify_all()

    def _random_sleep(self) -> None:
        time.sleep(random.randint(0, 1))


class Director(threading.Thread):
    def __init__(self, semaphore: threading.Semaphore, cv: threading.Condition) -> None:
        super().__init__()
        self.sem: threading.Semaphore = semaphore
        self.cv: threading.Condition = cv

    def run(self) -> None:
        while True:
            with self.cv:
                self.cv.wait()
                if self._need_more_tickets():
                    self._add_tickets()
                    self._release_tickets()

    def _need_more_tickets(self) -> bool:
        global TOTAL_TICKETS
        return TOTAL_TICKETS <= 1

    def _add_tickets(self) -> None:
        global TOTAL_TICKETS
        added_tickets = random.randint(1, 10)
        logger.info(f"Director added {added_tickets} tickets")
        TOTAL_TICKETS += added_tickets

    def _release_tickets(self) -> None:
        with self.sem:
            self.sem.release()


def main() -> None:
    semaphore: threading.Semaphore = threading.Semaphore()
    condition_variable: threading.Condition = threading.Condition()
    sellers: List[Seller] = []
    for _ in range(3):
        seller = Seller(semaphore, condition_variable)
        seller.start()
        sellers.append(seller)

    director = Director(semaphore, condition_variable)
    director.start()

    for seller in sellers:
        seller.join()

    director.join()


if __name__ == "__main__":
    main()
