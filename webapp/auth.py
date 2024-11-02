from flask import (
    Blueprint,
    render_template ,
    redirect , 
    url_for , 
    request , 
    session,
    flash
)
from models import User , File

auth_app = Blueprint('auth' , __name__)

class Login:
    def controler(self , username , password):
        user_result = User.get_or_none(User.username == username)
        if user_result:
            print("a")
            pass_result1 = User.get(User.username == username)
            if pass_result1.password == password:
                return True
            else:
                return False
        else:
            print(user_result)
            return False
    
class Register(Login):
    def controler(self, username , email):
        username_get = User.get_or_none(User.username == username)
        email_get = User.get_or_none(User.email == email)
        if username_get or email_get == 1:
            print(email_get , username_get)
            return 1
        else:
            return 0
    
class AuthFactory:
    def factoryType(type):
        if type == "login":
            return Login()
        elif type == "register":
            return Register()
        else:
            raise ValueError("value is invalid type !")
        



@auth_app.route("/register" , methods=["GET" , "POST"])
def registerPage():
    if request.method =="POST":
        username_get = request.form["username"]
        password_get = request.form["password"]
        email_get = request.form["email"]

        auth = AuthFactory.factoryType(type="register")
        result = auth.controler(username = username_get , email=email_get)
        if result == 1:
            flash("user or password is already exists !" , "error")
        else:
            print(result)
            session["username"] = username_get
            User.create(username = username_get , password = password_get , email=email_get)
            return redirect(url_for("view.dashboard"))
    if session.get("username"):
        return redirect(url_for("view.dashboard"))
    return render_template("register.html")

@auth_app.route("/login" , methods=["GET" , "POST"])
def loginPage():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        auth = AuthFactory.factoryType(type="login")
        result = auth.controler(username=username , password=password)

        if result == False:
            flash("username or password is not correct !")
        else:
            session["username"] = username
            return redirect(url_for("view.dashboard"))
    if session.get("username"):
        return redirect(url_for("view.dashboard"))
    return render_template("login.html")