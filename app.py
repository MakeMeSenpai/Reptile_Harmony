#All TESTS FAIL, ENSURE THAT TESTS PASS BEFORE RUNNING
from flask import Flask, request, render_template

#names our url path and give it our static pages
app = Flask(__name__, static_url_path='')

#Our flask page routes :3
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/shop")
def shop():
    return render_template("shop.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")

@app.route("/other")
def other():
    return render_template("other.html")