import unittest
from passlock import User,Credentials

def logo():






 def create_new_user(username,password):
    '''
    function to create a new user with a username and password
    '''
    new_user = User(username,password)
    return new_user

def save_user(username,password):
    '''
    function to save a new user
    '''
    User.save_user(username,password)


def display_user():
    '''
    function to display existing user
    '''
    return User.display_user()


def login_user(username,password):
    '''
    function that checks whether a user exist and then login the user on
    '''
    check_user = Credentials.verify_user(username,password)
    return check_user
def create_new_user(account,userName,password):
    '''
    function creates new credentials for the user
    '''
    new_credentials =Credentials(account,userName,password)
    return new_credentials

def save_credentials(credentials):
    '''
    function that saves user credentials
    '''
    credentials.save_credentails(credentials)
def display_account_detials():
    '''
    function that returns all the saved user credentals
    '''
    return Credentials.display_credentials()

def delete_credetials():
    '''
    functions that delete user credentails from credentials list
    '''
    Credentials.delete_credentials()

def find_credentials(account,userName):
    '''
    function that finds user credentials by an account details
    '''
    return Credentials.find_credentials(account,[userName])

def check_credentials(account,userName):
    '''
    function that check if credentials exists from credentials list
    '''
    return Credentials.if_credential_exit(account,userName)


def generate_password():
    '''
    function that generate random password
    '''
    auto_password = Credentials.generate_password()
    return auto_password

def copy_password(account):
    '''
    funtion that copies password  using pyperclip framework
    '''
    return Credentials.copy_password(account)


def main():
    print("Hello Welcome to your Accounts Password Store...\n Please enter one of the following to proceed.\n CA ---  Create New Account  \n LI ---  Have An Account  \n")
    short_code=input("").lower().strip()
    if short_code == "ca":
        print("Sign Up")
        print('*' * 50)
        username = input("User_name: ")
        while True:
            print(" TP - To type your own pasword:\n GP - To generate random Password")
            password_Choice = input().lower().strip()
            if password_Choice == 'tp':
                password = input("Enter Password\n")
                break
            elif password_Choice == 'gp':
                password = generate_password()
                print("your password is being generated")
                break
            else:
                print("invalid choice please try again....")
                return  print(" TP - To type your own pasword:\n GP - To generate random Password")
                     
        save_user(create_new_user(username,password))
        print("*"*'safelock')
        print(f"Hello {username}, Your account has been created succesfully! Your password is: {password}")
        print("*"*'safelcok')

    elif short_code == "li":
        print("*"'safelock')
        print("Enter your User name and your Password to log in:")
        print('*''safelcok')
        username = input("User name: ")
        password = input("password: ")
        login = login_user(username,password)
        return print("hera are your credentials"+ login)
    if login_user == Credentials.verify_user(username,password):
            print(f"Hello {username}.Welcome To PassWord Locker Manager")  
            print('safelcok')
    while True:
        print("Use these short codes:\n CC - Create a new credential \n DC - Display Credentials \n FC - Find a credential \n GP - Generate A randomn password \n D - Delete credential \n EX - Exit the application \n")
        short_code = input().lower()
        if short_code == "cc":
            print("Create New Credential")
            print("."'safelock')
            input('enter account name:')
            account = input().lower()
            print("Your Account username")
            userName = input()
            while True:
                print(" TP - To type your own pasword if you already have an account:\n GP - To generate random Password")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    password = input("Enter Your Own Password\n")
                    break
                elif password_Choice == 'gp':
                    password = generate_password()
                    break
                else:
                    print("Invalid password please try again")
            save_credentials(create_new_user(account,userName,password))
            print('\n')
            print(f"Account Credential for: {account} - UserName: {userName} - Password:{password} created succesfully")
            print('\n')
        elif short_code == "dc":
            if display_account_detials():
                print("Here's your list of acoounts: ")
                 
                print('*' * 30)
                print('_'* 30)
                for account in display_account_detials():
                    print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                    print('_'* 30)
                print('*' * 30)
            else:
                print("You don't have any credentials saved yet..........")
        elif short_code == "fc":
            print("Enter the Account Name you want to search for")
            search_name = input().lower()
            if find_credentials(search_name):
                search_credential =find_credentials (search_name)
                print(f"Account Name : {search_credential.account}")
                print('-' * 50)
                print(f"User Name: {search_credential.userName} Password :{search_credential.password}")
                print('-' * 50)
            else:
                print("That Credential does not exist")
                print('\n')
        elif short_code == "d":
            print("Enter the account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credentials(search_name):
                search_credential = find_credentials(search_name)
                print("_"*50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print("That Credential you want to delete does not exist in your store yet")

        elif short_code == 'gp':

            password = generate_password()
            print(f" {password} Has been generated succesfull. You can proceed to use it to your account")
        elif short_code == 'ex':
            print("Thanks for using passwords store manager.. See you next time!")
            break
        else:
            print("Wrong entry... Check your entry again and let it match those in the menu")
    else:
        print('please enter valid input')


if __name__ == '__main__':
    unittest.app
