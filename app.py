from flask import Flask, jsonify
import math

# Crear la aplicacion Flask
app = Flask(__name__)
#ruta de inicio
@app.route('/')
def inicio():
    return jsonify({"mensaje": "Bienvenido al microservicio"})
#ruta calcular el factorial y determinar si es par o impar
@app.route('/numero/<int:n>', methods=['GET'])
def numero(n):
    if n < 0:
        return jsonify({
            "error": "No se puede calcular el factorial de un número negativo"
        }), 400

    factorial = math.factorial(n)

    if n % 2 == 0:
        etiqueta = "par"
    else:
        etiqueta = "impar"
    resultado = {
        "status": "ok",
        "numero_recibido": n,
        "factorial": factorial,
        "etiqueta del numero recibido por url": etiqueta
    }

    return jsonify(resultado)

if __name__ == '__main__':
    app.run(debug=True)
