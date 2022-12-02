from flask import Flask, render_template, request
from uuid import uuid4
import pandas as pd
import csv


app = Flask(__name__)


# le o itens.csv e joga para o index.html
@app.route('/')
def index():
    with open('filmes.csv', 'rt') as file_in:
        filmes = csv.DictReader(file_in)
        return render_template('home.html', filmes=filmes)


#sei la como funciona (não modificar)
@app.route('/create')
def create():
    return render_template('create.html')


#salva as variaveis do forms em uma nova row no arquivo .csv
@app.route('/save', methods=['POST'])
def save():

    #puxa as variaveis do forms 
    name = request.form['name']         
    avaliacao = request.form['avaliacao'] 
   

    entrada= []
    entrada.append([uuid4(), name, avaliacao]) #trocar para pandas dataset dps aaaaaaaaaaaaaaa

    #adiciona *append* uma nova row no .csv
    with open('filmes.csv', 'a') as file_out:
        escritor = csv.writer(file_out)
        escritor.writerows(entrada)
   
    #redireciona para "/" 
    with open('filmes.csv', 'rt') as file_in:
        filmes = csv.DictReader(file_in)
        return render_template('home.html', filmes=filmes)


#deleta rows de acordo com o Id
@app.route('/delete/<id>')
def delete(id):

    # abre o arquivo .csv pelo pandas
    data = pd.read_csv("filmes.csv") 
    #seta o index valeu para a columm 'Id'
    data = data.set_index("id") 

    #dropa toda row que tiver a mesma variavel "id" na columm index
    data.drop(id, axis='index', inplace=True) 
    
    #salva o novo dataset
    data.to_csv('filmes.csv')  

    # função que le o arquivo e envia a variavel para o html OBS: provavelmente existe alguma outra forma mais simples e eficiente de fazer isso, porem esta funcionando ent deia quieto 
    with open('filmes.csv', 'rt') as file_in:
        filmes = csv.DictReader(file_in)
        return render_template('home.html', filmes=filmes)
    

#pega as variaveis da row que o usuario quer modificar e coloca dentro dos forms
@app.route('/edit/<id>/<name>/<avaliacao>')
def update(id,name,avaliacao):#obtem as var pela url 
    lista = [id,name,avaliacao]#transforma em lista para facilitar
    return render_template('edit.html', lista=lista) #e joga para o update.html


#salva os forms que foram modificados do /update/
@app.route('/saveedit', methods=['POST'])
def saveedit():

    #obtem as novas variaveis
    id = request.form['id'] # o id esta ocultado na pagina
    name = request.form['name']         
    avaliacao = request.form['avaliacao'] 
 

    #abre o dataframe do .csv
    data = pd.read_csv("filmes.csv")

    #cria um novo dataframe apartir das novas variaveis
    new_df = pd.DataFrame({'id': [id],'name': [name],'avaliacao': [avaliacao]})

    #seta os index's para a coluna 'Id'
    #n sei se isso é necessario mas na minha mente faz sentido 
    data = data.set_index("id")
    new_df = new_df.set_index("id")

    #atualiza os dados do data frame antigo com o novo
    data.update(new_df)

    #salva o arquivo
    data.to_csv('filmes.csv')

    #redireciona para "/"
    with open('filmes.csv', 'rt') as file_in:
        filmes = csv.DictReader(file_in)
        return render_template('home.html', filmes=filmes)

app.run(debug=True)
