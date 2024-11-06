from extention import app
from models import User
from flask import render_template

if User.get_or_none(User.admin == "1"):
    pass
else:
    super_username_input = input("this is a input username and password for\ncreate super user\ntype your username: ")
    super_email_input = input("type your email :")
    super_password_input = input("type your password :")
    User.create(username = super_username_input , email=super_email_input , password=super_password_input , admin="1")

@app.errorhandler(404)
def notfoundPage(error):
    return render_template("404.html") , 404

app.run(debug=True)