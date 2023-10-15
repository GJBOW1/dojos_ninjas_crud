from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.ninjas import Ninjas
from flask_app.models.dojos import Dojos

@app.route('/add/ninja', methods=["POST"])
def adding_ninja():
    dojos = Dojos.get_dojos()
    return render_template("add_ninja.html", dojos = dojos)

@app.route('/adding/ninja', methods=["POST"])
def ninja_added():
    Ninjas.save(request.form)
    ninjas = Ninjas.get_ninjas_dojo(request.form)
    return render_template("ninja_success.html", ninjas = ninjas)