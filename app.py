from flask import Flask, render_template
# from flask_mysqldb import MySQL


app = Flask(__name__)

app.secret_key = 'key'


# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = ''
# app.config['MYSQL_DB'] = 'advance'


# mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
    