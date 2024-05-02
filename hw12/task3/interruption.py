from threading import Semaphore, Thread
import time
import signal

semaphore = Semaphore()
exit_flag = False


def worker_1():
    global exit_flag
    while not exit_flag:
        semaphore.acquire()
        print(1)
        semaphore.release()
        time.sleep(0.25)


def worker_2():
    global exit_flag
    while not exit_flag:
        semaphore.acquire()
        print(2)
        semaphore.release()
        time.sleep(0.25)


def handle_interrupt(signum, frame):
    global exit_flag
    exit_flag = True
    print("\nKeyboard interrupt, quit.")


thread_1 = Thread(target=worker_1)
thread_2 = Thread(target=worker_2)

signal.signal(signal.SIGINT, handle_interrupt)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
