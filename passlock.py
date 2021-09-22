import random
import string


class User:
    '''
    class that generates new instance of a user
    '''

    user_list = []

    def __init__(self,username,password):

        '''
        method that defines the properties of user
        '''

        self.username = username
        self.password = password




    def  save_user(self):

        '''
        method that saves a new instances into the user list
        '''
        User.user_list.append(self)


    @classmethod
    def display_user():
        return cls.user_list



    def delete_user(self):

        '''
        method that delete user details
        '''
        self.user_list.remove(self)


class Credentials:

    '''
    credentials class that create new objects for credentials
    '''

    Credentials_list =[]

   



    


    



