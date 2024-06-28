from flask import Flask, render_template, request
import csv

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
        # Receive all the info from the HTML form.
        location = request.form.get('location')
        date = request.form.get('date')
        time = request.form.get('time')
        is_repeating = request.form.get('frequency')

        #Check id the plan is repeating or not.
        if eval(is_repeating):
            with open('Flask Web App/repeating.csv','a') as csv_repeating:
                csv_repeating.write(f'\n{location},{date},{time}')
            csv_repeating.close()
        else:
            with open('Flask Web App/onetime.csv','a') as csv_onetime:
                csv_onetime.write(f'\n{location},{date},{time}')
            csv_onetime.close()
        return render_template('suggested.html')
    return render_template('suggest.html')

# Should be removed before uploading
app.run(debug=True)

