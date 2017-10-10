from threading import Thread

class Count(Thread):


  Result=0

  def run(self):
     for i in range(10000):
         Count.Result += 1
         Count.Result -=1

     Count.Result += 1

for i in range(10000):
    Count().start()
print(Count.Result)

