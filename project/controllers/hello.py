from project import app
from flask import render_template, request, redirect, url_for

#route index
@app.route('/', methods=["GET", "POST"])
def index():
    render_template('index.html.j2')
