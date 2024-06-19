import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def bianca_scrapper():
    url = 'http://bianca.com'
    html = requests.get(url).text
    sopa = BeautifulSoup(html, 'html.parser')
    titulo = sopa.find('title').text

    texto = sopa.find('h1').text

    retorno = {'title':titulo, 'text':texto}
    print(retorno)
    return jsonify(retorno)

@app.route('/test')
def test():
    return 'teste'

app.run(debug = False)