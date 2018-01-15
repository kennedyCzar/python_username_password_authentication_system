# python_username_password_authentication_system
user information(including username and password) management system. New user can create an account if it doesn’t conflict with any existing one while exisiting user can return to the system using his username and password. A suggested outline of the program is as below:

def newusers():
    enter a name
    if the name is used in the system:
        enter again
    else:
        set the password
    … …

def oldusers():
    Enter the  username and password
    if password is right:  
        print(name, 'welcome back ')  
    else:  
        print('login incorrect')  
    … …

def login():
    option = """
            (N)ew User Login 
            (O)ld User Login
            (E)xit """
    Enter the option
    … …

if __name__ == '__main__':  
    login()  
    
