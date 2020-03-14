from flask import Flask, request
import csv
import json
import os
import subprocess
import config

app = Flask(__name__)


def get_table_data_by_csv():
    file_path = 'static/output/data2.csv'
    table_data = []
    with open(file_path, 'rt', encoding="utf8")as f:
        data = csv.reader(f)
        headers = next(data, None)
        garbage = next(data, None)
        for row in data:
            table_data.append(row)
    return table_data


def test():
    filepath = os.path.join(config.project_dir(), 'static\\output\\' 'data2.csv')


def run_spider(form_data):
    spider_name = "fmarket"
    cat = form_data['cat']
    location = form_data['location']
    print(location + cat)
    # filepath = os.path.join(config.project_dir(), 'static\\output\\' 'data2.json')
    subprocess.call(
        ['scrapy', 'crawl', spider_name, '-a', 'f_data='+form_data['location'] + ',' + form_data['cat'] + ',' +
         form_data['search_term']+','+form_data['radius']])

    # subprocess.check_output(['scrapy', 'crawl', spider_name, "-o", 'xyz1.csv'])


def get_table_data_by_json():
    # file_path = 'static/output/abc.json'
    filepath = os.path.join(config.project_dir(), 'static\\output\\' 'data2.json')
    table_data = []
    with open(filepath, 'rt', encoding="utf8") as f:
        data = json.load(f)
        headers = next(data, None)
        # garbage = next(data, None)
        for row in data:
            table_data.append(row)
    return table_data


def get_form_data():
    cat = request.form['category']
    location = request.form['loc']
    search_term = request.form['skey']
    radius_in_km = request.form['radius']
    form_data = {
        'cat': cat,
        'location': location,
        'search_term': search_term,
        'radius': radius_in_km,
        'result': 3
    }
    return form_data

    # test()
