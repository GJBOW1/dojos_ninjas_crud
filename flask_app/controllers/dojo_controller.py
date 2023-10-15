from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.dojos import Dojos
from flask_app.models.ninjas import Ninjas


@app.route('/', methods=['GET', 'POST'])
def home():
    dojos = Dojos.get_dojos()
    return render_template('index.html', dojos = dojos)


@app.route('/add/dojo', methods=["POST"])
def adding_dojo():
    data = {
        "name": request.form["name"]
    }
    Dojos.save(data)
    return redirect("/")

@app.route('/user/created', methods=["GET", "POST"])
def create_user():
    data = {
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"]
        }
    Dojos.save(data)
    return redirect('/user/display')

@app.route('/dojo/display', methods=["GET", "POST"])
def displaying():
    users = Dojos.get_users()
    return render_template('new_dojo.html', users = users)


@app.route('/dojo/<int:id>')
def show(id):
    data= {
        "id":id
    }
    ninjas = Ninjas.show_ninja(data)
    dojos = Dojos.get_dojos_group(data)
    return render_template('display_dojo.html', dojos = dojos, ninjas = ninjas)








# @app.route("/dojo/delete/<int:id>")
# def delete(id):
#     data= {
#         "id":id
#     }
#     Dojos.delete_dojo(data)
#     return redirect('/')

# @app.route("/<int:id>")
# def updating(id):
#     data= {
#         "id":id
#     }
#     user = Dojos.show_dojo(data)
#     return render_template("update_dojo.html", dojo = dojo)

# @app.route("/update/<int:id>", methods=["POST"])
# def update(id):
#     data = {
#         "id": id,
#         "first_name":request.form["first_name"],
#         "last_name":request.form["last_name"],
#         "email":request.form["email"]
#     }
#     Dojos.update_dojo(data)
#     return redirect('/')