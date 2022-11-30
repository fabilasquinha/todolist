from flask import Flask , render_template , request
import pandas
import csv
import uuid

app = Flask(__name__)

filmes = []

@app.route('/')
def home(): 
    #templates
    return render_template('home.html' , filmes=filmes)

#Salva as variáveis no form em um arquivo.csv
@app.route('/create' , methods=['POST'])
def create():

    #Onde puxa as variáveis forms
    name = request.form['name']
    avaliacao = request.form['avaliacao']
    entrada.append([uuid4(), nome, avaliação])

    #Adicionar uma nova row no .csv
    with open():
        filme = {'name' : name, 'avaliacao': avaliacao}
        filmes.append(filme)
        return render_template('home.html' , filmes=filmes)

@app.route('/delete', methods=['DELETE'])
def delete(task):
    task = {'name' : name, 'avaliacao': avaliacao}
    tasks.delete(tasks)
    return render_template('home.html' , tasks=tasks)

app.run(debug=True)