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
                password = generate_Password()
                break
   



