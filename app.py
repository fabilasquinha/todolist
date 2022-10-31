from flask import Flask

app = Flask(__name__)

@app.route('/')
def nome():
    return 'hello web'

app.run(debug=True)