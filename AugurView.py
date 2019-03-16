#!/usr/bin/python2.7
from flask import Blueprint, render_template, current_app, jsonify
from .. import doc_builder
view = Blueprint('AugurView',__name__,template_folder="templates",static_folder="static")


@view.route("/")
def index():
    return render_template("view/view.html.jinja")

@view.route("/getEndpoints")
def getEndpoints():
    docs = doc_builder.endpoint_docs
    out = []
    for doc in docs:
        if doc['method'] == "POST":
            t = {}
            t['route'] = doc['route']
            t['description'] = doc['title']
            out += [t]
    return jsonify(out)

# Context Processor
@view.context_processor
def inject_debug():
    ## This is used to determine which jQuery file should be loaded by the user
    return dict(debug=current_app.debug)
