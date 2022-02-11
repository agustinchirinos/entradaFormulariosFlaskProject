from flask import render_template, request, render_template_string
from jinja2 import Markup

from . import xssreflejado

@xssreflejado.route('/')
def index():  # put application's code here
    return render_template("index.html")

@xssreflejado.route("/reflejado1/", methods=["GET","POST"])
def reflejado1():
    if request.method == "POST":
        comentario = request.form.get("comentario")
        return comentario
    return render_template("reflejado1.html")

@xssreflejado.route("/reflejado2/", methods=["GET","POST"])
def reflejado2():
    if request.method == "POST":
        comentario = request.form.get("comentario")
        return render_template_string(comentario)
    return render_template("reflejado2.html")

@xssreflejado.route("/reflejado3/", methods=["GET","POST"])
def reflejado3():
    comentario = ""
    if request.method == "POST":
        comentario = request.form.get("comentario")
    return render_template("reflejado3.html", comentario=Markup(comentario))

@xssreflejado.route("/reflejado4/", methods=["GET","POST"])
def reflejado4():
    comentario = ""
    if request.method == "POST":
        comentario = request.form.get("comentario")
    return render_template("reflejado4.html", comentario=comentario)

@xssreflejado.route("/reflejado5/", methods=["GET","POST"])
def reflejado5():
    comentario = ""
    if request.method == "POST":
        comentario = request.form.get("comentario")
    return render_template("reflejado5.html", comentario=comentario)

@xssreflejado.route("/reflejado6/", methods=["GET","POST"])
def reflejado6():
    comentario = ""
    estilo = ""
    if request.method == "POST":
        estilo = request.form.get("estilo")
        comentario = request.form.get("comentario")
    return render_template("reflejado6.html", comentario=comentario, estilo=estilo)

@xssreflejado.route("/reflejado7/", methods=["GET","POST"])
def reflejado7():
    texto = ""
    url = ""
    if request.method == "POST":
        url = request.form.get("url")
        texto = request.form.get("texto")
    return render_template("reflejado7.html", url=url, texto=texto)
