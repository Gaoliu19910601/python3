'''threading functions with a lock'''

import threading
import time

# tlock = threading.Lock()

def timer(name, delay, repeat):
    print("Timer: "+name+" has started")

    # tlock.acquire()
    # print(name+' has been locked')

    while repeat > 0:
        time.sleep(delay)
        print(name+' :'+str(time.ctime(time.time())))
        repeat -=1

    # print(name + ' has been released')
    # tlock.release()


    print(name+': is complete')


def Main():
    t1 = threading.Thread(target=timer, args=('timer1',2,5))
    t2 = threading.Thread(target=timer, args=('timer2',3,5))

    t1.start()
    t2.start()

    print('Main completed')

if __name__ == '__main__':
    Main()

