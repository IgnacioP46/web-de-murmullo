# -*- coding: iso-8859-15 -*-
import json
import sys

from flask import Flask, request, render_template
murmullo = Flask(__name__)

total_discos = 0

@murmullo.route("/", methods=['GET'])
def home():
    return murmullo.send_static_file("index.html")


@murmullo.route("/login", methods=['GET'])
def login():
    return murmullo.send_static_file("LonginMurmullo.html")


@murmullo.route("/singup", methods=['GET'])
def signup():
    return murmullo.send_static_file("SingUpMurmullo.html")

@murmullo.route("/carrito",methods=["GET" , "POST"])
def carrito():
    return render_template("carrito.html")


@murmullo.route("/processcarrito", methods=['GET', 'POST'])
def processcarrito():
    with open('templates\\infodiscos.json') as f:
        jsondoc = json.load(f)
        posicion = int(request.form.get("posicion"))
        print(posicion)
        precio = jsondoc["discos"][posicion]["precio"]
        titulo = jsondoc["discos"][posicion]["titulo"]
        print(precio)
    global total_discos
    monto = request.form.get("monto")
    monto = int(monto)
    #precio = request.form.get("precio")
    precio = int(precio)
    total_discos = total_discos + monto
    precio_total = precio * monto
    print("total_discos")
    return render_template("carrito.html" , respuesta = request.form , total = total_discos, precio_total = precio_total, titulo = titulo)



@murmullo.route("/processSignup", methods=['GET', 'POST'])
def processSignup():
    missing = []
    fields = ["nombre", "apellidos","direccion", "piso_y_puerta", "otras_indicaciones", 'email', 'passwd','confirm', 'signup_submit']
    for field in fields:
        value = request.form.get(field, None)
        if value is None:
            missing.append(field)
        if missing:
              return "Warning: Some fields are missing" + str(missing)

    return render_template("datos.html", respuesta = request.form)
        
@murmullo.route("/processLogin", methods=['GET', 'POST'])
def processLogin():
	missing = []
	fields = ['email', 'passwd', 'signup_submit']
	for field in fields:
		value = request.form.get(field, None)
		if value is None:
			missing.append(field)
	if missing:
		return "Warning: Some fields are missing"

	return render_template(template_name_or_list="datos.html" , respuesta = request.form)

#app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# start the server with the 'run()' method
if __name__ == '__main__':
    murmullo.run(debug=True, port=80)