from flask import Flask , render_template , request
from uuid import uuid4
import pandas as pd
import csv


app = Flask(__name__)

filmes = []

@app.route('/')
def index():
    with open('filmes.csv', 'rt') as file_in:
        dados = csv.DictReader(file_in)
        return render_template('home.html', dados=dados)

@app.route('/html')
def home(): 
    #templates
    return render_template('create.html' , filmes=filmes)

#Salva as variáveis no form em um arquivo.csv
@app.route('/create' , methods=['POST'])
def create():

    #Onde puxa as variáveis forms
    name = request.form['name']
    avaliacao = request.form['avaliacao']
    filmes.append([uuid4(), name, avaliacao])

    #Adicionar uma nova row no .csv
    with open('filmes.csv','a') as file_out:
        usuario = csv.writer(file_out)
        usuario.writerows(filmes)
    
    #Redireciona as variáveis para '/'
    with open('filmes.csv', 'rt') as file_in:
        dados = csv.DictReader(file_in)
        return render_template('home.html', dados=dados)

#Pega as variáveis para modificar
@app.route('/edit/<nome>/<avaliacao>')
def edit(nome,avaliacao):
    editList = [nome,avaliacao]
    return render_template('edit.html', editList=editList)

#Onde salva as variáveis modificadas
@app.route('/saveEdit', methods=['SAVE'])
def saveEdit():

    #Inseri as novas variáveis
    nome = request.form['nome']
    avaliacao = request.form['avaliacao']

    #Abre o DataFrame do .csv
    dataFrame = pd.read.csv('filmes.csv')

    #Criação do novo DataFrame
    new_dataFrame = pd.DataFRame({'nome': [nome],'avaliacao': [avaliacao]})

    #Colocar os index para a coluna 'nome'
    dataFrame = dataFrame.set_index('nome')
    new_dataFrame = new_dataFrame.set_index("nome")

    #Atualiza o DataFrame
    dataFrame.update(new_dataFrame)

    #Salva o nome DataFrame no .csv
    dataFrame.to_csv('filmes.csv')

    #Redireciona as variáveis para '/'
    with open('filmes.csv', 'rt') as file_in:
        dados = csv.DictReader(file_in)
        return render_template('home.html', dados=dados)

#Deleta as linhas pelo Id
@app.route('/delete/<id>')
def delete(id):

    #Abre o arquivo pelo pandas
    dataFrame = pd.read_csv("filmes.csv") 

    #Coloca o index para coluna 'id'
    dataFrame = dataFrame.set_index("Id") 

    #Pega toda a linha que tiver a mesma variavel "id" na coluna index
    dataFrame.drop(id, axis='index', inplace=True) 
    
    #Salva o novo DataFrame
    dataFrame.to_csv('filmes.csv')  

    #Le o arquivo e envia para a variável do Html 
    with open('filmes.csv', 'rt') as file_in:
        dados = csv.DictReader(file_in)
        return render_template('home.html', dados=dados)

app.run(debug=True)