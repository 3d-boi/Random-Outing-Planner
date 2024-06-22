from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/voteyes')
def voteyes():
    print('someone voted Yes')
    return render_template('vote.html')

@app.route('/voteno')
def voteno():
    print('someone voted No')
    return render_template('vote.html')

@app.route('/suggest')
def suggest():
    return render_template('suggest.html')

# Should be removed before uploading
app.run(debug=True)

