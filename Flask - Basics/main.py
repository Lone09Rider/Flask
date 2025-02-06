# from flask import Flask, render_template, redirect, request, url_for, make_response

# app = Flask(__name__)


# @app.route("/", methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         name = request.form['user_name']
#         age = request.form['age']
#         return render_template('display.html', data=name, age = age)
#     return render_template('form_base.html')

# if __name__ == "__main__":
#     app.run(debug=True)