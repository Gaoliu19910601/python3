
import logging

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

filehandler = logging.FileHandler('employee.log')
filehandler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(filehandler)

# logging.basicConfig(filename='employee.log', level=logging.INFO, format='%(asctime)s:%(name)s:%(message)s')


class Employee(object):

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        logger.info('Created {}-{}-{}'.format(self.first, self.last, self.pay))

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


