# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 01:40:25 2018

@author: kennedy
"""
#sample --> 'kennedy':'ify1', 'andy': 'best56', 'great': 'op3'
#create new user
system = {} #database system
option = ""
def newusers():
    uname= input("Enter a username: ")
    if uname in system:
        print("User already exit: Create new user")
    else:
        pw = input("Enter password: ")
        system[uname] = pw
        print("\nUser created: welcome to the network")
        
#login for old users      
def oldusers():
    uname = input("Enter your username:")
    pw = input("Enter your password: ")
    if uname in system and system[uname] == pw:
        print(uname, 'Welcome back')
    else:
        print('Login incorrect')
        

#login
def login():
    #option = {'New': 1, 'Old': 2, 'Exit': 3}
    option = input("Enter an option: N --> New User, O-->OldUser,E-->Exit ")
    if option == "N":
        newusers()
    elif option == "O":
        oldusers()
    elif option == "E":
        exit
                
#we call the main function
if __name__ == "__main__":
    login()