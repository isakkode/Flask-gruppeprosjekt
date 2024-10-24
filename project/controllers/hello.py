from project import app
from flask import render_template, request, redirect, url_for


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html.j2')


@app.route('/order-car.html.j2', methods=["GET", "POST"])
def order_car():
    if request.method == "POST":
        result = request.form.to_dict()
        print(result)
    return render_template('order-car.html.j2')


@app.route('/cancel-order-car.html.j2', methods=["GET", "POST"])
def return_order_car():
    if request.method == "POST":
        result = request.form.to_dict()
        
    return render_template('cancel-order-car.html.j2')


@app.route('/rent-car.html.j2', methods=["GET", "POST"])
def rent_car():
    if request.method == "POST":
        result = request.form.to_dict()
        print(result)
    return render_template('rent-car.html.j2')


@app.route('/return-car.html.j2', methods=["GET", "POST"])
def return_car():
    if request.method == "POST":
        result = request.form.to_dict()
        print(result)
    return render_template('return-car.html.j2')
