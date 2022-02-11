from html import escape

from flask import request, render_template

from . import xssalmacenado
from .. import engine


@xssalmacenado.route("/xssalmacenadocreate/",methods=["GET","POST"])
def xssalmacenadocreate():
    if request.method == "POST":
        titulo = request.form.get("titulo")
        mensaje = request.form.get("mensaje")
        sql = f"INSERT INTO posts (titulo,mensaje) VALUES ('{titulo}','{mensaje}')"
        with engine.connect() as conn:
            conn.execute(sql)
    return render_template("xssalmacenadocreate.html")

@xssalmacenado.route("/xssalmacenadoindex/")
def xssalmacenadoindex():
    sql = f"SELECT * FROM posts"
    with engine.connect() as conn:
        posts = conn.execute(sql)
    return render_template("xssalmacenadoindex.html", posts=posts)