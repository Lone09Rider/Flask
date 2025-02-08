from flask import Flask
import pymysql

app = Flask(__name__)

# Database connection details
db_host = 'localhost'
db_user = 'root'
db_password = 'root'
db_name = 'flask_example'

def create_table():
    # Connect to the database
    connection = pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )

    try:
        with connection.cursor() as cursor:
            # SQL query to create a table
            create_table_query = """
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL UNIQUE
            )
            """
            cursor.execute(create_table_query)
            connection.commit()
    finally:
        connection.close()

@app.route('/')
def index():
    create_table()
    return "Table created successfully!"

if __name__ == '__main__':
    app.run(debug=True)