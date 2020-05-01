from flask import render_template

from . import main

@main.errorhandler(404)
def 404(404):

    return render_template('404.html')