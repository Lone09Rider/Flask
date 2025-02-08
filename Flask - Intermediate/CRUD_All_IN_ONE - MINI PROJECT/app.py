from flask import Flask, request, render_template, url_for, redirect
import pymysql

app = Flask(__name__)

def create_con_db():
    # Connect to MySQL server without specifying a database
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root"
    )
    
    try:
        # CREATE DB IF NOT THERE
        db_sql = "CREATE DATABASE IF NOT EXISTS school"
        connection.cursor().execute(db_sql)
        connection.commit()
        
        # Select the newly created database
        connection.select_db('school')
        
        # CREATE TABLE
        table_sql = """CREATE TABLE IF NOT EXISTS students(
                id int primary key auto_increment,
                name varchar(30),
                age varchar(30)
            )"""
            
        connection.cursor().execute(table_sql)
        connection.commit()
    finally:
        connection.close()
    

@app.route("/", methods=['GET', 'POST'])
def create():
    create_con_db()
    if request.method == 'POST':
        name = request.form['username']
        age = request.form['age']
        
        # INSERT
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database="school"
        )
        
        try:
            insert_sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
            cursor = connection.cursor()
            cursor.execute(insert_sql, (name, age))
            connection.commit()
        finally:
            connection.close()
        
        return render_template('data.html')
    
    return render_template('index.html')

# To Fetch
@app.route("/students", methods=['GET'])
def fetch_students():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="school"
    )
    
    try:
        fetch_sql = "SELECT * FROM students"
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(fetch_sql)
        students = cursor.fetchall()
        print(students)  # Debug print to check fetched data
    finally:
        connection.close()
    
    return render_template('students.html', students=students)

# Delete
@app.route("/delete/<int:id>", methods=['POST'])
def delete_student(id):
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="school"
    )
    
    try:
        delete_sql = "DELETE FROM students WHERE id = %s"
        cursor = connection.cursor()
        cursor.execute(delete_sql, (id,))
        connection.commit()
    finally:
        connection.close()
    
    return redirect(url_for('fetch_students'))

# Update
@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update_student(id):
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database="school"
    )
    
    try:
        if request.method == 'POST':
            name = request.form['username']
            age = request.form['age']
            
            update_sql = "UPDATE students SET name = %s, age = %s WHERE id = %s"
            cursor = connection.cursor()
            cursor.execute(update_sql, (name, age, id))
            connection.commit()
            
            return redirect(url_for('fetch_students'))
        
        fetch_sql = "SELECT * FROM students WHERE id = %s"
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute(fetch_sql, (id,))
        student = cursor.fetchone()
    finally:
        connection.close()
    
    return render_template('update.html', student=student)

if __name__ == "__main__":
    app.run(debug=True)