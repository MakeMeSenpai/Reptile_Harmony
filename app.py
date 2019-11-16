#All TESTS FAIL, ENSURE THAT TESTS PASS BEFORE RUNNING
from flask import Flask, request, render_template

app = Flask(__name__)

#Our flask page routes :3
#all html is bootrap reliant, bootstrap does not seem to be in any effect here.
# ensure that css3 passes through from static page before doing any manjor changes. 
# Then follow README page instructions. 
@app.route("/")
def index():
    return render_template("index.html")

#shop does not run. maybe a needed renaming in templates
@app.route("/shop")
def shop():
    return render_template("shop.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")

@app.route("/other")
def other():
    return render_template("other.html")