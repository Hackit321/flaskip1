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




