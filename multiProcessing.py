from multiprocessing import Process
import time

def func1():
    time.sleep(2)
    print('Func1: Başlatıldı')
    time.sleep(2)
    print('Func1: Sonlandırıldı')
    time.sleep(2)

def func2():
    time.sleep(2)
    print('Func2: Başlatıldı')
    time.sleep(2)
    print('Func2: Sonlandırıldı')
    time.sleep(2)

def mainFun():
    print('mainFun: Başlatıldı')
    time.sleep(2)
    p1 = Process(func1())
    p2 = Process(func2())
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('mainFun: Sonlandırıldı')

if __name__ =='__main__':
    mainFun()
