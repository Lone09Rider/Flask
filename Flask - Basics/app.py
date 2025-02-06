# from flask import Flask, render_template, redirect, url_for

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template("index.html")

# @app.route("/home")
# def home():
#     return render_template('index.html', data = "SRj is the one who's everywhere but nowhere!!")

# @app.route("/redirect_1")
# def ex_1():
#     return redirect(url_for("index"))

# @app.route("/redirect_2")
# def ex_2():
#     return redirect(url_for("home"))

# if __name__ == "__main__":
#     app.run(debug=True)