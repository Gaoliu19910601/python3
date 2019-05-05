import logging
from employee_tut20 import Employee,  logger

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s') # The format

filehandler = logging.FileHandler('sample.log') # Setting log file name
filehandler.setFormatter(formatter) # Setting the format for this handler

streamhandler = logging.StreamHandler() # Displays the log statements in the console
streamhandler.setFormatter(formatter) # Setting the format for this handler

logger2 = logging.getLogger(__name__) # to specify path
logger2.setLevel(logging.DEBUG) # only Debug statements in the log file
logger2.addHandler(filehandler) # Adding the handler
logger2.addHandler(streamhandler) # Adding the handler

filehandler.setLevel(logging.ERROR) # Only shows the error in the log file

# logging.basicConfig(filename='sample.log', level=logging.DEBUG, format='%(asctime)s:%(name)s:%(message)s')

num1 = 24

num2 = 0

add_result = num1+num2
logger2.debug('Add: {} + {} = {}'.format(num1, num2, add_result))

sub_result = num1-num2
logger2.debug('Sub: {} - {} = {}'.format(num1, num2, sub_result))

mul_result = num1*num2
logger2.debug('Mul: {} * {} = {}'.format(num1, num2, mul_result))

try:
    div_result = num1/num2
except ZeroDivisionError:
    logger2.exception('Tried to divide by Zero') # Shows both this statement and the traceback
    # logger2.error('Tried to divide by Zero') # Just shows this statement



emp1 = Employee('parle', 'biscot', 450000)
emp2 = Employee('third reich', 'furer', 230000)

logger.info('Ivan peru {}'.format(emp1.fullname))
logger.info('Ivan peru {}'.format(emp2.fullname))