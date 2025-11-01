from flask import Flask,render_template,request,redirect,url_for,flash
from forms import RegistrationForm

app = Flask(__name__)
app.secret_key = "my_secret_key"

@app.route('/',methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        flash(f"Welcome {name} ! You are registered successfully !","success")
        return redirect(url_for("success",name=name))
    return render_template('register.html',form=form)



@app.route("/success")
def success():
    name = request.args.get("name")
    return render_template("success.html",name=name)