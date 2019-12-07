from flask import Flask
from flask import jsonify
from bs4 import BeautifulSoup
import os
import json
from crawl import crawl as crawl_horosopes
from storage import download_file

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config['JSON_AS_ASCII'] = False

@app.route('/',methods=['GET'])
def get():
    return json.loads(download_file())

@app.route('/crawl',methods=['GET'])
def crawl():
    return crawl_horosopes()

if __name__ == "__main__":
    app.run()
