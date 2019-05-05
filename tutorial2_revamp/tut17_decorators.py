
print('')
print("------------------EXAMPLE-1 GENERAL-----------------------------")
print('')


def decorator_func(original_function):
    def wrapper_func(*args, **kwargs):
        print('This was printed before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs)
    return wrapper_func


# class decorator_class(object):
#     def __init__(self,original_function):
#         self.original_function = original_function
#
#     def __call__(self, *args, **kwargs):
#         print('This was printed before {}'.format(self.original_function.__name__))
#         return self.original_function(*args,**kwargs)


@decorator_func
def display():
    print('Hey today is wonderful!')


@decorator_func
def display2(name, age):
    print("{} told today was wonderful. His age is just {}".format(name,age))


# display()
display2('John', 34)


print('')
print("------------------EXAMPLE-2 LOGGING DECORATORS-----------------------------")
print('')


from functools import wraps


def my_logger(original_func):

    import logging

    formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')  # The format
    filehandler = logging.FileHandler(filename = '{}.log'.format(original_func.__name__))  # Setting log file name
    filehandler.setFormatter(formatter)  # Setting the format for this handle

    logger = logging.getLogger(__name__)  # to specify path

    logger.setLevel(logging.INFO)  # only Debug statements in the log file
    logger.addHandler(filehandler)  # Adding the handler

    @wraps(original_func)
    def wrapper_func2(*args,**kwargs):
        logger.info('Ran with args: {} and kwargs: {}'.format(args, kwargs))
        return original_func(*args,**kwargs)

    return wrapper_func2


name = ['amar','deep','viki','kumar','kokki']
job = ['civil','mech','EIE','ECE','IBT']


@my_logger
def display3(name2,job2):
    print("{} told today was wonderful. He works in {}".format(name2,job2))

import random
display3(random.choice(name),random.choice(job))


print('')
print("------------------EXAMPLE-2 TIMING DECORATORS-----------------------------")
print('')

def my_timer(original_func):

    import time

    @wraps(original_func)
    def wrapper_func3(*args, **kwargs):

        t1 = time.time()
        amar =  original_func(*args, **kwargs)
        t2 = time.time()-t1

        print('The {} function took {} seconds'.format(original_func.__name__, t2))

        return amar

    return wrapper_func3


@my_logger
def display4(name,age):
    # import time
    # time.sleep(1)
    print("{} told today was wonderful. His age is just {}".format(name,age))

display4('Harold',98)


print('')
print("------------------EXAMPLE-3 MULTIPLE DECORATORS-----------------------------")
print('')



@my_timer
@my_logger
def multiple_dec(name,job):
    print("{} told that he was working as a {}.".format(name,job))

multiple_dec(random.choice(name),random.choice(job))

print('')
print("------------------EXAMPLE-3 DECORATORS WITH ARGS-----------------------------")
print('')


def decorator_prefix(prefix):
    def decorator_function(original_function):
        def wrapper_func(*args,**kwargs):
            print(prefix,'This was printed before {}'.format(original_function.__name__))
            result =  original_function(*args,**kwargs)
            print(prefix,'This was printed after {}'.format(original_function.__name__))
            return result
        return wrapper_func
    return decorator_function


@decorator_prefix('TESTING: ')
def display_info6(name,job):
    print("{} told that he was working as a {}.".format(name,job))


display_info6(random.choice(name),random.choice(job))


