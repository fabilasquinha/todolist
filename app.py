from flask import Flask , render_template , request

app = Flask(__name__)

tasks = [
    {'name' : 'estudar' , 'avaliacao' : '2/10'},
    {'name' : 'dormir' , 'avaliacao' : '10/10'}
]

@app.route('/')
def home():
    #templates
    return render_template('home.html' , tasks=tasks)

@app.route('/create' , methods=['POST'])
def create():
    name = request.form['name']
    avaliacao = request.form['avaliacao']
    #number = request.form['number']
    task = {'name' : name, 'avaliacao': avaliacao}
    tasks.append(task)
    return render_template('home.html' , tasks=tasks)

@app.route('/delete', methods=['DELETE'])
def delete(task):
    task = {'name' : name, 'avaliacao': avaliacao}
    tasks.delete(tasks)
    return render_template('home.html' , tasks=tasks)

app.run(debug=True)