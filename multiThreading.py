import threading
from threading import Thread
import time

def func1():
    time.sleep(2)
    print('Func1: Başlatıldı')
    time.sleep(2)
    print('Func2: Sonlandırıldı')
    time.sleep(2)

def func2():
    time.sleep(2)
    print('Func2: Başlatıldı')
    time.sleep(2)
    print('Func2: Sonlandırıldı')
    time.sleep(2)

def mainFunc():
    print('mainFunc: Başlatıldı')
    t1 = threading.Thread(target=func1())
    t2 = threading.Thread(target=func2())
    t1.start()
    t2.start()
    print('mainFunc: Sonlandırıldı')

mainFunc()