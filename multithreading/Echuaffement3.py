from threading import Thread, RLock
verrou=RLock()

class Count(Thread):


  Result=0


  def run(self):

     for i in range(1000):
         with verrou:
          Count.Result += 1
          Count.Result -=1

     Count.Result += 1


thread_list = []
for i in range(1000):
    thread_list.append(Count())

for t in thread_list:
    t.start()

for t in thread_list:
    t.join()

print(Count.Result)

