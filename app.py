from flask import Flask, render_template, redirect, request, url_for
from flask_mysqldb import MySQL
from helper import functions

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'fbmarketdb'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('main.html')


@app.route('/list', methods=['GET', 'POST'])
def archive_list():
    return render_template('data_list.html')


@app.route('/item_list', methods=['GET', 'POST'])
def item_list():
    # form_data = functions.get_form_data()
    fb_items = get_all_fb_items()
    # functions.run_spider(form_data)
    if request.method == 'POST':
        form_data = functions.get_form_data()
        functions.run_spider(form_data)
        return redirect(url_for('item_list'))
    else:
        return render_template('item_list.html', data=fb_items)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


def get_all_fb_items():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM fb_item")
    fb_data = cur.fetchall()
    cur.close()
    return fb_data


if __name__ == '__main__':
    app.run(debug=True)
