from flask import render_template, request
from sqlalchemy import text
from werkzeug.datastructures import CombinedMultiDict

from app import engine
from .forms import FormWTF
from .models import Cliente
from . import contramedidas


@contramedidas.route("/formwtf/", methods=["GET","POST"])
def formwtf():
    form = FormWTF(CombinedMultiDict((request.files, request.form)))
    if form.validate_on_submit():
        return form.nombre.data
    return render_template("formulariowtf.html", form=form)

@contramedidas.route("/sqlinjectionindexparametrizada/",methods=["GET","POST"])
def sqlinjectionindexparametrizada():
    id = 0
    sql = f"SELECT * FROM productos"
    if request.method == "POST":
        id = request.form.get("id")
        sql = text("SELECT * FROM productos WHERE id= :id")
        with engine.connect() as conn:
            productos = conn.execute(sql,id=id)
            return render_template("sqlinjectionindexparametrizada.html", productos=productos, id=id)
    with engine.connect() as conn:
        productos = conn.execute(sql)
    return render_template("sqlinjectionindexparametrizada.html", productos=productos, id=id)

@contramedidas.route("/ormindex/",methods=["GET","POST"])
def ormindex():
    if request.method == "POST":
        id = request.form.get("id")
        clientes = Cliente.query.filter_by(id=id)
    else:
        clientes = Cliente.query.all()
    return render_template("ormindex.html",clientes=clientes)