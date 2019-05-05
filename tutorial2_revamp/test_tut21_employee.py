
import tut21_employee
import unittest

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupclass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('Setup')
        self.emp1 = tut21_employee.Employee('Amardeep','Amavasai',1000000)
        self.emp2 = tut21_employee.Employee('jabajaba','yadayada',500000)

    def tearDown(self):
        print('teardown \n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp1.email,'Amardeep.Amavasai@gmail.com')
        self.assertEqual(self.emp2.email,'jabajaba.yadayada@gmail.com')

        self.emp1.first = 'Amith'
        self.emp2.first = 'jadakooba'

        self.assertEqual(self.emp1.email,'Amith.Amavasai@gmail.com')
        self.assertEqual(self.emp2.email,'jadakooba.yadayada@gmail.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp1.fullname,'Amardeep Amavasai')
        self.assertEqual(self.emp2.fullname,'jabajaba yadayada')

        self.emp1.first = 'Amith'
        self.emp2.first = 'jadakooba'

        self.assertEqual(self.emp1.fullname,'Amith Amavasai')
        self.assertEqual(self.emp2.fullname,'jadakooba yadayada')




if __name__ == '__main__':
    unittest.main()
