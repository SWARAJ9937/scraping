from flask import Flask , render_template
app = Flask (__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/swaraj')
def swaraj():
    return 'hi , swaraj bhai2'

app.run(debug=True)