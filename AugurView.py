#!/usr/bin/python2.7
from flask import Blueprint, render_template, current_app

view = Blueprint('AugurView',__name__,template_folder="templates",static_folder="static")


@view.route("/")
def index():
    return render_template("view/view.html.jinja")


# Context Processor
@view.context_processor
def inject_debug():
    ## This is used to determine which jQuery file should be loaded by the user
    return dict(debug=current_app.debug)
