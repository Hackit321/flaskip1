from _typeshed import Self
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
    def display_user(cls):
        '''
        function that returns the display user detials
        '''

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

    @classmethod
    def verify_user(cls,username,password):

        '''
        method that check if username and credentials match or else return a message
        
        '''

        for user in User.user_list():
            if user.username == username and user.password == password :
                a_user = user.username and user.password

                return a_user
            else:
                print('wrong username or password')

    def __init__(self,acccount,userNamme,password):
        '''
        function that defines user credentials
        '''
        self.account = acccount
        self.uerName =userNamme
        self.password = password
        

    def save_credentials(self):
        '''
        mehtod saves user credentials
        '''
        Credentials.Credentials_list.append(self)

    

    




   



    


    



