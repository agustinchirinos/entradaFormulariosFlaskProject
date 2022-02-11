from flask import request, render_template

from . import sqlinjection
from .. import engine


@sqlinjection.route("/sqlinjectionindex/",methods=["GET","POST"])
def sqlinjectionindex():
    id = 0
    sql = f"SELECT * FROM productos"
    if request.method == "POST":
        id = request.form.get("id")
        sql += f" WHERE id={id}"
    with engine.connect() as conn:
        productos = conn.execute(sql)
    return render_template("sqlinjectionindex.html", productos=productos, id=id)

@sqlinjection.route("/sqlinjectionlogin/", methods=["get","post"])
def sqlinjectionlogin():
    # usuario.rowcount
    # usuario.fetchone()[0]
    username = ""
    error = ""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        sql = f"SELECT * FROM usuarios WHERE username='{username}' AND password='{password}'"
        print(sql)
        with engine.connect() as conn:
            usuario = conn.execute(sql)
            if usuario.rowcount >= 1:
                return render_template("sqlinjectionwelcome.html",usuario=usuario.fetchone()[0])
            else:
                error = "Credenciales incorrectas"
    return render_template("sqlinjectionlogin.html", username=username, error = error)