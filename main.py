from flask import Flask, render_template
import requests
from flask_wtf import FlaskForm
from wtforms import HiddenField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret secret key'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = QuoteForm()
    quotes = None
    response = requests.get('http://api.quotable.io/quotes/random?limit=3')
    if response.status_code == 200:
       quotes = response.json()
       print(quotes)
    else:
       print("Failed to retrieve weather data")

    return render_template('index.html', quotes=quotes, form=form)


class QuoteForm(FlaskForm):
   csrf_token = HiddenField()

if __name__ == '__main__':
    app.run(debug=True)
