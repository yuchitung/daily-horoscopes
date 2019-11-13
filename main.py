from flask import Flask
from flask import jsonify
from bs4 import BeautifulSoup
import os
import json
from crawl import crawl as crawl_horosopes

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/',methods=['GET'])
def get():
    filepath = 'daily-horoscopes.json'
    if os.path.isfile(filepath):
        with open('daily-horoscopes.json') as json_file:
            data = json.load(json_file)
    else:
        data = 'data not found'
    return jsonify(data)

@app.route('/crawl',methods=['GET'])
def crawl():
    return crawl_horosopes()

if __name__ == "__main__":
    app.run()
