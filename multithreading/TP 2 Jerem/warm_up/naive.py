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

    for i in range(10000):
        CounterThread().start()

    print(CounterThread.COUNTER)
