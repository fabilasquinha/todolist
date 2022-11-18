from flask import Flask , render_template

app = Flask(__name__)

tasks = [
    {'name' : 'estudar' , 'finished' : False},
    {'name' : 'dormir' , 'finished' : True}
]

@app.route('/')
def home():
    #templates
    return render_template('home.html' , tasks=tasks)
@app.route('/bye')
def bye():
    return 'bye'

app.run(debug=True)