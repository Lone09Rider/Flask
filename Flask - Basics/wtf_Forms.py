from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import TextAreaField, PasswordField, SubmitField

app = Flask(__name__)
app.secret_key = 'your_secret_key'

class UserForm(FlaskForm):
    username = TextAreaField("Username : ")
    password = PasswordField("Enter your password !")
    submit = SubmitField("Enter Data")

@app.route("/", methods=['GET', 'POST'])
def form():
    form = UserForm()
    if request.method == 'POST' and form.validate_on_submit():
        return render_template('display_2.html')
    return render_template('wtform_base.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)