from threading import Thread, Lock
from random import *
from time import sleep
verrou=Lock()


class Document(Thread):
    ID = 1

    def __init__(self):
        Thread.__init__(self)
        self.ID = Document.ID
        self.page = randint(1, 10)
        Document.ID += 1

    def run(self):
        verrou.acquire()
        for i in range(1, self.page):
            sleep(0.5)
            print('Thread #{} : Page #{}'.format(self.ID, i))
        verrou.release()



for i in range(10):
    Document().start()






