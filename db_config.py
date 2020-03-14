from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'fbmarketdb'

mysql = MySQL(app)


def get_all_fb_items():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM fb_items")
    fb_data = cur.fetchall()
    cur.close()
    return fb_data
