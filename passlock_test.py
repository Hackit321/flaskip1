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
        '''
        test_init testcase that test if the object has been initialized correctly
        '''
        self.assertEquals(self.new_user.username,'mark')
        self.assertEquals(self.new_user.password,'mark002.')


    def test_save_user(self):
        '''
        test case to test if useer object is saved in the user list    
        '''
        self.new_user.save_user()
        self.assertEquals(len(User.user_list),1)

    
class TestCredentials(unittest.TestCase):
    '''
    A Test class that defines test case for the credentials
    '''
    def setUp(self):
        '''
        Mehtod that run each testcase
        '''
        new_credentials =Credentials(self,'Gmial','mark_kk','mark002.')

    def test_inti(self,account,userName,password):
            '''
            testcase method that check if user credentials instances have been initialized
            '''
            self.assertEquals(self.new_credentials.account,'Gmail')
            self.assertEquals(self.new_credenital.userName,'mark_kk')
            self.assertEquals(self.new_credentials.password,'mark002.')

    def test_save_credentials(self):
        '''
        testcase to check if credentials object is saved in credentials list
        '''
        self.new_credentials(self)
        self.new_credentials(len(Credentials.Credentials_list),1)



    def teaarDown(self):
        '''
        method that clean up after each test case has run
        '''
        Credentials.Credentials_list = []


   
            
   
        
