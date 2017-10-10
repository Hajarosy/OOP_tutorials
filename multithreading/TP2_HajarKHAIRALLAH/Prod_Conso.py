from threading import Thread
from random import randint
from time import sleep


class ProduceEntier(Thread):

    def __init__(self, file):
        Thread.__init__(self)
        self.filedattente=file
    def run(self):
        while True:
            a=randint(1,10)
            self.filedattente.append(a)
            sleep(randint(1,3))
            print('Ajoute {} a la file'.format(a))

class ConsumeEntier(Thread):
    def __init__(self, file):
        Thread.__init__(self)
        self.filedattente = file
    def run(self):
        if len(self.filedattente)==0:
          print("liste vide")
        else:
          sleep(randint(1, 3))
          print('Consomme {}'.format(self.filedattente.pop()))

filedattente=[1,3]
while (len(filedattente))>0:
 p=ProduceEntier(filedattente)
 c=ConsumeEntier(filedattente)
 p.start()
 c.start()
