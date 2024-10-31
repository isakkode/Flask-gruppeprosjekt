from project import app
from flask import render_template, request, redirect, url_for
from project.models.queries import book, cancel_booking, rent_car_query, return_car_query

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html.j2')


@app.route('/order-car.html.j2', methods=["GET", "POST"])
def order_car():
    data = None
    if request.method == "POST":
        result = request.form.to_dict()
        data = book(result["car-id"], result["customer-id"])

    return render_template('order-car.html.j2', data=data)


@app.route('/cancel-order-car.html.j2', methods=["GET", "POST"])
def return_order_car():
    data = None
    if request.method == "POST":
        result = request.form.to_dict()
        data = cancel_booking(result["car-id"], result["customer-id"])
     
    return render_template('cancel-order-car.html.j2', data=data)


@app.route('/rent-car.html.j2', methods=["GET", "POST"])
def rent_car():
    data = None
    if request.method == "POST":
        result = request.form.to_dict()
        data = rent_car_query(result["car-id"], result["customer-id"])

    return render_template('rent-car.html.j2', data=data)


@app.route('/return-car.html.j2', methods=["GET", "POST"])
def return_car():
    data = None
    if request.method == "POST":
        result = request.form.to_dict()
        data = return_car_query(result["car-id"], result["customer-id"], result["status"])
        
    return render_template('return-car.html.j2', data=data)
