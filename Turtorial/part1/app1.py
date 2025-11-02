# # # # from flask import Flask,request

# # # # app = Flask(__name__)

# # # # @app.route('/')
# # # # def home():
# # # #     return 'Hello user! This is my first flask app.'

# # # # @app.route('/about')
# # # # def about():
# # # #     return 'This is about us page.'

# # # # @app.route('/contact')
# # # # def contact():
# # # #     return 'This is a contact us page.'


# # # # @app.route('/submit',methods=["GET","POST"])
# # # # def submit():
# # # #     if request.method=="POST":
# # # #         return "You send data !"
# # # #     else:
# # # #         return "You are only viewing the page."


# # # from flask import Flask,request,redirect,url_for,session,Response

# # # app = Flask(__name__)
# # # app.secret_key = "supersecret"
# # # #homepage login page 
# # # @app.route('/',methods=["GET","POST"])
# # # def login():
# # #     if request.method == "POST":
# # #         username = request.form.get("username")
# # #         password = request.form.get("password")

# # #         if username == "admin" and password == "123":
# # #             session["user"] = username
# # #             return redirect(url_for("welcome"))
# # #         else:
# # #             return Response("In-valid credentials. Try again",mimetype="text/plain")
    
# # #     return '''

# # #     <h2>Login Page</h2>
# # #     <form method="POST">
# # #     Username: <input type="text" name="username"><br>
# # #     Password: <input type="password" name="password"><br>
# # #     <input type="submit" value="login">
# # #     </form>
# # #     '''


# # # #welcome page after login 
# # # @app.route("/welcome")
# # # def welcome():
# # #     if "user" in session:
# # #         return f'''
# # #         <h2>Welcome, {session["user"]} !</h2>
# # #         <a href={url_for('logout')}>Logout</a>
# # #         '''
# # #     return redirect(url_for('login'))

# # # @app.route('/logout')
# # # def logout():
# # #     session.pop("user",None)
# # #     return redirect(url_for('login'))
# # #     #session["user"] = hangthim



# # from flask import Flask,redirect,request,render_template

# # app = Flask(__name__)

# # @app.route("/")
# # def login():
# #     return render_template("login.html")

# # @app.route("/submit",methods=["POST"])
# # def submit():
# #     username = request.form.get("username")
# #     password = request.form.get("password")

# #     # if username=="hangthim" and password == "pass":
# #     #     return render_template("welcome.html",name=username)
# #     valid_users= {
# #         "admin":'123',
# #         'sagar123':'pass',
# #         'hangthim':'limbu',

# #     }
# #     if username in valid_users and password == valid_users[username]:
# #         return render_template('welcome.html',name=username)
# #     else:
# #         return "Invalid Credentials."


# from flask import Flask, render_template 

# app = Flask(__name__)

# app.route("/")
# def student_profile():
#     return render_template(
#         'profile.html',
#         name = "Hangthim",
#         is_topper = True,
#         subjects = ['science','maths','history']
#     )
