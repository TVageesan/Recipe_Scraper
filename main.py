from my_scraper import get_raw,get_urls
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")#displays current list of urls
def hello_world():
    return render_template("index.html",urls = get_urls())

@app.route('/shopping')#generates compiled shopping list
def shopping():
    raw_data = get_raw(get_urls())
    x = render_template("shopping.html",raw_data = raw_data)
    print(raw_data)
    return x
app.run(port=5002)