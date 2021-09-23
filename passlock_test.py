import unittest
from passlock import User,Credentials

class TestClass(unittest.TestCase):
    '''
    A Test class that defines test case for the user  behaviour
    '''
    def setUp(self) :
        '''
        set up mehtod that runs each testcase
        '''
        self.new_user = User('mark','mark002.')

        return super().setUp()
    
    def test_init(self):














class TestCredentials(unittest.TestCase):
    '''
    A Test class that defines test case for the credentials
    '''
