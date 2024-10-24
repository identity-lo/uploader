from flask import (
    Blueprint,
    render_template ,
    redirect , 
    url_for , 
    request , 
    session
)
import os
from extention_model import file , user

view_app = Blueprint('view' , __name__)
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@view_app.route("/")
def index():
    get_db = file.select()
    check_admin = session.get("admin")
    if check_admin :
        sup = "1"
        return render_template("index.html" , get_db=get_db , admin=sup)

    return render_template("index.html" , get_db=get_db)

@view_app.route("/dashboard")
def dashboard():
    if not session.get("username"):
        return redirect("/auth/login")
    get_db__file = file.select().where(file.user == session.get("username"))

    return render_template("dashboard.html" , files=get_db__file)

@view_app.route("/uploader" , methods=["GET" , "POST"])
def uploader():
    if request.method == "POST":
        if "file" not in request.files:
            print("a")
            return redirect(request.url)
        
        files = request.files["file"]

        if files.filename == '':
            print("b")
            return redirect(request.url)
        
        if files and allowed_file(files.filename):
            print("c")
            files.save(dst=os.path.join("\.files" , files.filename))
            file.create(user = session.get("username") , path = files.filename)
            return redirect("/dashboard")


    return render_template("uploader.html")

@view_app.route("/delete/<int:id>")
def deletefile(id):
    get_r = file.get(file.id == id)
    get_r.delete_instance()
    return redirect("/dashboard")

