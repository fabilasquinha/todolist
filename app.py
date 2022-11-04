from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def home():
    #templates
    return render_template('home.html')
@app.route('/bye')
def bye():
    return 'bye'

app.run(debug=True)