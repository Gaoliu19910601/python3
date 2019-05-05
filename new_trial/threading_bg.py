'''Runs a program in a background thread '''

import threading
import time

class AsyncWrite(threading.Thread):
    def __init__(self,text,out):
        threading.Thread.__init__(self)
        self.text = text
        self.out = out


    def run(self):
        fname = open(self.out,'a')
        fname.write(self.text+'\n')
        fname.close()
        time.sleep(2)
        print('Background thread function is complete and written to '+self.out)

def Main():
    message = input('give me an input:')
    background = AsyncWrite(message,'out.txt')
    background.start()

    i = 5

    while i > 0:
        print('looping...')
        time.sleep(2)
        i-=1

    background.join()
    print('Waited until thread is complete')

if __name__ == '__main__':
    Main()

