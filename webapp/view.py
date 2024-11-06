from flask import (
    Blueprint,
    render_template ,
    redirect , 
    url_for , 
    request , 
    session,
    send_file
)
import os
from models import User as user
from models import File as file

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
    global ad
    ad = None
    if session.get("username") == "amir_root":
        session["admin_val"] = "True"

    if not session.get("username"):
        return redirect(url_for("auth.loginPage"))
    
    if session.get("admin_val"):
        ad = True
    get_db__file = file.select().where(file.user == session.get("username"))

    return render_template("dashboard.html" , files=get_db__file , ad=ad)

@view_app.route("/uploader" , methods=["GET" , "POST"])
def uploader():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        
        files = request.files["file"]

        if files.filename == '':
            return redirect(request.url)
        
        if files and allowed_file(files.filename):
            files.save(dst=f"webapp/lfiles/{files.filename}")
            file.create(user = session.get("username") , path = files.filename)
            return redirect("/dashboard")


    return render_template("uploader.html")

@view_app.route("/uploads/<name>")
def download_file(name):
    return send_file(f"./lfiles/{name}")


@view_app.route("/delete/<int:id>")
def deletefile(id):
    get_r = file.get(file.id == id)
    get_r.delete_instance()
    for root, dirs, files in os.walk("webapp/lfiles"):
        if get_r.path in files:
            os.remove(f"webapp/lfiles/{get_r.path}")
    return redirect("/dashboard")

