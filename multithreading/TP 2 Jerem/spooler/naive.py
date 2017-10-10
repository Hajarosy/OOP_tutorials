# std
from random import randint
from threading import Thread
from time import sleep


class Document(Thread):

    ID = 1

    def __init__(self):
        super().__init__()
        self.id = Document.ID
        # The number of pages is a random number between 1 and 10
        self.pages = randint(1, 10)
        # We increment the id at the end so that every thread has an unique id
        Document.ID += 1

    def run(self):
        # For every page we are going to print, we wait 0.5s (time to print)
        # and then we display the line
        for page in range(1, self.pages + 1):
            sleep(0.5)
            print('Thread #{} : page #{}'.format(self.id, page))


if __name__ == '__main__':
    for i in range(15):
        Document().start()
