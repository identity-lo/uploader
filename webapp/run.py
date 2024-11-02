from extention import app
from models import User

if User.get_or_none(User.admin == "1"):
    pass
else:
    super_username_input = input("this is a input username and password for\ncreate super user\ntype your username: ")
    super_email_input = input("type your email :")
    super_password_input = input("type your password :")
    User.create(username = super_username_input , email=super_email_input , password=super_password_input , admin="1")

app.run(debug=True , host="192.168.43.251")