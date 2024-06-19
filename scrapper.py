import requests
import os
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)
os.environ['PORT'] = '4000'

@app.route('/')
def bianca_scrapper():
    url = 'http://bianca.com'
    html = requests.get(url).text
    sopa = BeautifulSoup(html, 'html.parser')
    titulo = sopa.find('title').text

    texto = sopa.find('h1').text

    retorno = {'title':titulo, 'text':texto}
    return jsonify(retorno)

app.run(debug = False)
