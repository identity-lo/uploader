from flask import (
    Blueprint,
    render_template ,
    redirect , 
    url_for , 
    request , 
    session,
    flash
)
from extention_model import user , file

auth_app = Blueprint('auth' , __name__)

class AuthControler:

    def __init__(self , username=None , email=None , password=None):
        self.username = username
        self.email = email
        self.password = password



    
    def Login(self):
        pass


@auth_app.before_request
def check_user():
    admin = user.select().where(user.admin == "True")
    check = session.get("username")
    for i in admin:
        if i.username:
            session["admin"] = "True"
    if check:
        return redirect("/login")

@auth_app.route("/register" , methods=["GET" , "POST"])
def registerPage():
    if request.method =="POST":
        dbru = user.select().where(user.username==request.form["username"])
        dbre = user.select().where(user.username ==request.form["email"])
        if not dbru or dbre:
            session["username"] = request.form["username"]
            user.create(
                username = request.form["username"] , 
                password = request.form["password"] , 
                email=request.form["email"]
            )
            return redirect("/dashboard")
        else:
            flash("username or email is already exists !" , category="error")
            return render_template("register.html")
    return render_template("register.html")

@auth_app.route("/login" , methods=["GET" , "POST"])
def loginPage():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # authc = AuthControler(
        #     username=username,
        #     password=password
        # )
        # result = authc.Login()
        username_db = user.select().where(user.username == username)
        for ii in username_db:
            global password_db
            password_db = ii.password

        if username_db:
            if password_db:
                return redirect(url_for("dashboard"))
            else:
                print("password")
                flash("username or password is not correct !")
                return render_template("login.html")
        else:
            print("username")
            flash("username or password is not correct !")
            return render_template("login.html")
    return render_template("login.html")