from models import *

def Register():
        username = User.select().where(User.username == "amirali")
        email = User.select().where(User.email == "harchi@gmail.com")
        global r_username
        global r_email
        r_username = None
        r_email = None
        
        for i in username:
            if username:
                r_username = i.username
                print(r_username)
                

        for i in email:
            if email:
                print(i)
                r_email=email
        
        if r_email or r_username:
            print("t")
        else:
            print("f")
Register()