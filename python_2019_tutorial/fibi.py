#!usr/bin/python

import argparse
import time

start_time = time.clock()

def fib(n):
    a ,b = 0,1
    for i in range(n):
        a, b = b, a+b
    return a


parser = argparse.ArgumentParser()

group = parser.add_mutually_exclusive_group()
group.add_argument("-v",'--verbose',action='store_true')
group.add_argument('-q','--quiet',action='store_true')

parser.add_argument('num',help='The number you want.',type=int)
parser.add_argument('-o','--output',help='writes the file to a txt file',\
                     action = 'store_true')
args = parser.parse_args()

result = fib(args.num)

if args.verbose:
    print('The result is '+str(result))
elif args.quiet:
    print(str(result))
else:
    print('Fib('+str(args.num)+') = '+str(result))

if args.output:
    f = open('fibonacci.txt','a')
    f.write(str(result)+'\n')
    f.close


print('Total execution time: '+ str(time.clock()-start_time)+' secs')