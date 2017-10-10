# std
from threading import Thread, Lock


class CounterThread(Thread):

    COUNTER = 0

    def __init__(self):
        super().__init__()
        self.count_lock = Lock()

    def run(self):
        for i in range(10000):
            self.count_lock.acquire(True)
            CounterThread.COUNTER += 1
            CounterThread.COUNTER -= 1
            self.count_lock.release()

            self.count_lock.acquire()
        CounterThread.COUNTER += 1
        self.count_lock.release()


if __name__ == '__main__':
    thread_list = []
    for i in range(10000):
        CounterThread().start()
    print(CounterThread.COUNTER)
