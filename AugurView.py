#!/usr/bin/python2.7
from flask import Blueprint, render_template

view = Blueprint('AugurView',__name__,template_folder="templates",static_folder="static")


@view.route("/")
def index():
    return render_template("view/template.html.jinja")
