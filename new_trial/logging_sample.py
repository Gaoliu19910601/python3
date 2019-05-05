
import logging

# import class_complete_addendum

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("test.log")
file_handler.setLevel(logging.ERROR)

file_handler.setFormatter(logging.Formatter('%(asctime)s:%(name)s:%(message)s'))

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(logging.Formatter('%(asctime)s:%(name)s:%(message)s'))

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


# logging.basicConfig(filename="test.log",level=logging.DEBUG,\
#                     format='%(asctime)s:%(lineno)d:%(name)s:%(message)s')


num1 = 105

num2 = 0

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def div(x,y):
    try:
        result = x / y
    except ZeroDivisionError:
        # print("Cannot divide by zero")
        logger.error("Cannot divide by Zero")
        # logger.exception("CANNOT DIVIDE BY ZERO")
    else:
        return result

def multi(x,y):
    return x*y



add_result = add(num1,num2)
logger.debug("The added result of {} and {} is {}.".format(num1,num2,add_result))

sub_result = sub(num1,num2)
logger.debug("The subtracted result of {} and {} is {}.".format(num1,num2,sub_result))

div_result = div(num1,num2)
logger.debug("The divided result of {} and {} is {}.".format(num1,num2,div_result))

mul_result = multi(num1,num2)
logger.debug("The multiplied result of {} and {} is {}.".format(num1,num2,add_result))