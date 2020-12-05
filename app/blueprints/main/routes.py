from .import bp as main
from flask import current_app as app, render_template

@main.route('/')
def index():
    return render_template('index.html')

    