from flask import Flask, render_template, request

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

@app.route('/suggest', methods = ["GET","POST"])
def suggest():
    if request.method == "POST":
        location = request.form.get('location')
        date = request.form.get('date')
        time = request.form.get('time')
        return render_template('suggested.html')
    return render_template('suggest.html')

# Should be removed before uploading
app.run(debug=True)

