from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/registertocamp", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    input_email = request.form.get("email")
    return render_template("hello.html", email=input_email, name=input_name, age=input_age)

@app.route("/calculateskisize", methods=["POST"])
def calculate_skisize():
    input_height = request.form.get("height")
    input_skill = request.form.get("skill")
    
    output_skisize = round(int(input_height) * 0.9 * (1 + 0.1*(int(input_skill) - 2)),0)
    
    return render_template("skisize.html", size = output_skisize, height = input_height, skill = input_skill)