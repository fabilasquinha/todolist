from flask import Flask , render_template , request
from uuid import uuid4
import pandas as pd
import csv


app = Flask(__name__)

filmes = []

@app.route('/')
def index():
    with open('filmes.csv', 'rt') as file_in:
        dados = csv.DictReader(fole_in)
        return render_template('home.html', dados=dados)

@app.route('/html')
def home(): 
    #templates
    return render_template('home.html' , filmes=filmes)

#Salva as variáveis no form em um arquivo.csv
@app.route('/create' , methods=['POST'])
def create():

    #Onde puxa as variáveis forms
    name = request.form['name']
    avaliacao = request.form['avaliacao']
    filmes.append([uuid4(), nome, avaliação])

    #Adicionar uma nova row no .csv
    with open('filmes.csv','a') as file_out:
        usuario = csv.writer(file_out)
        usuario.writerows(filmes)
    
    #Redireciona as variáveis para '/'
    with open('filmes.csv', 'rt') as file_in:
        dados = csv.DictReader(file_in)
        return render_template('home.html', dados=dados)

app.run(debug=True)