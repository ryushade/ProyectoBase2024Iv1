from flask import Flask, render_template, request, redirect, flash, jsonify
import controlador_discos, controlador_artistas

app = Flask(__name__)

@app.route("/agregar_disco")
def formulario_agregar_disco():
    return render_template("agregar_disco.html")


@app.route("/guardar_disco", methods=["POST"])
def guardar_disco():
    codigo = request.form["nombre"]
    nombre = request.form["nombre"]
    artista = request.form["artista"]
    precio = request.form["precio"]
    genero = request.form["genero"]
    controlador_discos.insertar_disco(codigo, nombre, artista, precio, genero)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/discos")


@app.route("/")
@app.route("/discos")
def discos():
    discos = controlador_discos.obtener_discos()
    return render_template("discos.html", discos=discos)


@app.route("/eliminar_disco", methods=["POST"])
def eliminar_disco():
    controlador_discos.eliminar_disco(request.form["id"])
    return redirect("/discos")


@app.route("/formulario_editar_disco/<int:id>")
def editar_disco(id):
    # Obtener el disco por ID
    disco = controlador_discos.obtener_disco_por_id(id)
    return render_template("editar_disco.html", disco=disco)


@app.route("/actualizar_disco", methods=["POST"])
def actualizar_disco():
    id = request.form["id"]
    codigo = request.form["codigo"]
    nombre = request.form["nombre"]
    artista = request.form["artista"]
    precio = request.form["precio"]
    genero = request.form["genero"]
    controlador_discos.actualizar_disco(codigo, nombre, artista, precio, genero, id)
    return redirect("/discos")

##artistas
@app.route("/artistas")
def artistas():
    artistas = controlador_artistas.obtener_artistas()
    return render_template("artistas.html", artistas=artistas)
@app.route("/agregar_artista")
def formulario_agregar_artista():
    return render_template("agregar_artista.html")

@app.route("/guardar_artista", methods=["POST"])
def guardar_artista():
    nombre = request.form["nombre"]
    nacionalidad = request.form["nacionalidad"]
    controlador_artistas.insertar_artista(nombre, nacionalidad)
    return redirect("/artistas")

@app.route("/editar_artista/<int:id>")
def editar_artista(id):
    artista = controlador_artistas.obtener_artista_por_id(id)
    return render_template("editar_artista.html", artista=artista)

@app.route("/actualizar_artista", methods=["POST"])
def actualizar_artista():
    id = request.form["id"]
    nombre = request.form["nombre"]
    nacionalidad = request.form["nacionalidad"]
    controlador_artistas.actualizar_artista(nombre, nacionalidad, id)
    return redirect("/artistas")
@app.route("/eliminar_artista", methods=["POST"])
def eliminar_artista():
    controlador_artistas.eliminar_artista(request.form["id"])
    return redirect("/artistas")
# Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
