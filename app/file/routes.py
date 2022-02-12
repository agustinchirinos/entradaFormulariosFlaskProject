import os
from os.path import dirname, abspath, join

from flask import request, render_template
from werkzeug.utils import secure_filename

from . import file


@file.route("/fileupload/",methods=["GET","POST"])
def fileupload():
    msg = ""
    if request.method == "POST":

        url_dir = "app/static/upload/"
        file = request.files['fichero']
        file.save(url_dir+"/"+file.filename)
    return render_template("fileupload.html", msg=msg)


@file.route("/fileexecute/")
def fileexecute():
    # Obtener la lista de ficheros y pasarlos al template
    # Si han seleccionado un fichero ejecutar su contenido
    url_dir = "app/static/upload/"
    msg = ""
    filename = request.args.get("filename")
    ficheros = obtenerFicheros(url_dir)
    if filename:
        contenido = leerFichero(filename)
        exec(contenido)
        msg = "Fichero ejecutado correctamente"
    return render_template("fileexecute.html", ficheros=ficheros, msg=msg)

@file.route("/fileindex/")
def fileindex():
    # Obtener la lista de ficheros y pasarlos al template
    # Si han seleccionado un fichero mostrar su contenido
    contenido = ""
    url_dir = 'app/static/upload'
    filename = request.args.get("filename")
    ficheros = obtenerFicheros(url_dir)
    # print(os.getcwd())
    if filename:
        contenido = leerFichero(filename)


    return render_template("fileindex.html", ficheros=ficheros, contenido=contenido)

##########################################################
#   FUNCIONES AUXILIARES
##########################################################

def obtenerFicheros(url_dir):
    dir = os.listdir(url_dir)
    listaficheros = []
    for fichero in dir:
        if os.path.isfile(os.path.join(url_dir, fichero)):
            listaficheros.append(fichero)
    return listaficheros

def leerFichero(filename):
    contenido = ""
    with open(filename, "r") as file:
        for linea in file:
            contenido += linea
        return str(contenido)