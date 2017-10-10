# std
from random import randint
from threading import Thread, Lock
from time import sleep


class Document(Thread):

    ID = 1

    def __init__(self, lock):
        super().__init__()
        self.id = Document.ID
        # The number of pages is a random number between 1 and 10
        self.pages = randint(1, 10)

        # We add the lock so that every thread will run one at the time
        self.lock = lock

        # We increment the id at the end so that every thread has an unique id
        Document.ID += 1

    def run(self):
        # We first acquire the lock, so that we are sure this thread will run
        # alone
        self.lock.acquire()
        # For every page we are going to print, we wait 0.5s (time to print)
        # and then we display the line
        for page in range(1, self.pages + 1):
            sleep(0.5)
            print('Thread #{} : page #{}'.format(self.id, page))
        # At the end, we release the lock so that the next thread can print
        self.lock.release()


if __name__ == '__main__':
    # In order for the threads to be locked, every thread will share the same
    # Lock object
    thread_lock = Lock()
    for i in range(15):
        Document(thread_lock).start()
