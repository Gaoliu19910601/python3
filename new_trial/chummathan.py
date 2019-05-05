#!usr/bin/python

from string import Template
import time

start_time = time.clock()

class myTemplate(Template):
    delimiter = "#"


def Main():
    cart = []
    cart.append(dict(item='coke',price=12,qty=2))
    cart.append(dict(item='cake',price=22,qty=4))
    cart.append(dict(item='paste',price=52,qty=8))
    cart.append(dict(item='puff',price=62,qty=3))


    t = Template('$item * $qty = $price')
    total = 0
    for data in cart:
        print(t.substitute(data))
        total += data['price']
    print('The total is =' + str(total))
    print('Total execution time: '+ str(time.clock()-start_time)+' secs')

if __name__ == '__main__':
    Main()

# print(cart)
