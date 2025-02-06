import os
from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = r"C:\Users\srj00\Desktop\Flask\File Read\img"
app.config["SECRET_KEY"] = "SRj"

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect("/")
        file = request.files['file']
        if file.filename == '':
            return '<script>alert("File not Selected !!")</script>'
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return '<script>alert("File successfully uploaded")</script>'
    return render_template_string('''
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
    ''')

if __name__ == "__main__":
    app.run(debug=True)