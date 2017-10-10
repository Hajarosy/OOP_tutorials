# std
from threading import Thread


class CounterThread(Thread):

    COUNTER = 0

    def run(self):
        for idx in range(10000):
            CounterThread.COUNTER += 1
            CounterThread.COUNTER -= 1
        CounterThread.COUNTER += 1


if __name__ == '__main__':
    threads = []
    for i in range(10000):
        threads.append(CounterThread())

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print(CounterThread.COUNTER)
