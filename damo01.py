from threading import Thread
from time import sleep,ctime
class MyThread(Thread):
    def __init__(self, target =None, args =(),kwargs ={}):
        super().__init__()
        self.target = target
        self.args = args
        self.kwargs = kwargs


    def player(self):
        return self.target(*self.args,**self.kwargs)

    def run(self):
        self.player()


####################################
#测试函数 player(sec,song)
def player(sec,song):
    for i in range(3):
        print("playing%s:%s"%(song,ctime()))
        sleep(sec)

t = MyThread(target = player,args = (3,),kwargs = {"song":"凉凉"})
t.start()#以一个线程去执行
t.join()