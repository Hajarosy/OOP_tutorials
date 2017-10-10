# std
from queue import Queue
from random import randint
from threading import Thread
from time import sleep


class Producer(Thread):

    def __init__(self, queue):
        # In order to share the elements between the 2 threads these threads
        # need to use the same queue
        super().__init__()
        self.waiting_list = queue

    def run(self):
        # While true will enable to run the program indefinitely
        while True:
            # We put the thread on pause for a random number of seconds
            # between 1 and 3in order to take into account the production time
            sleep(randint(1, 3))
            random_int = randint(1, 10)
            # Then we add the random int in the queue
            self.waiting_list.put(random_int)
            print('Adding {} to the queue'.format(random_int))

        print('Shutting down the Producer thread')


class Consumer(Thread):

    def __init__(self, queue):
        super().__init__()
        # In order to share the elements between the 2 threads these threads
        # need to use the same queue
        self.waiting_list = queue

    def run(self):
        # While true will enable to run the program indefinitely
        while True:
            # If we don't have any elements in our queue, we just put the
            # consumer on hold
            while not self.waiting_list.qsize():
                sleep(0.1)
            # When the first element appears we enter in the normal process
            # First we consume the element during 1 to 3 seconds
            sleep(randint(1, 3))
            # And then we display the element consumed
            print('Consuming element {}'.format(self.waiting_list.get()))


if __name__ == '__main__':
    q = Queue()
    p = Producer(q)
    c = Consumer(q)
    p.start()
    c.start()
