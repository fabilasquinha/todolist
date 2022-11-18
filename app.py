from flask import Flask , render_template , request

app = Flask(__name__)

tasks = [
    {'name' : 'estudar' , 'finished' : False},
    {'name' : 'dormir' , 'finished' : True}
]

@app.route('/')
def home():
    #templates
    return render_template('home.html' , tasks=tasks)

@app.route('/create' , methods=['POST'])
def create():
    name = request.form['name']
    #number = request.form['number']
    task = {'name' : name, 'finished': False}
    tasks.append(task)
    return render_template('home.html' , tasks=tasks)

app.run(debug=True)