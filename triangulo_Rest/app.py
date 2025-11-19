from flask import Flask, request, jsonify
from models.triangulo import calcular_triangulo

app = Flask(__name__)

@app.route("/api/triangulo", methods=["POST"])
def calcular_triangulo_endpoint():

    # 1. Verificar que el cuerpo venga en formato JSON
    if not request.is_json:
        return jsonify({"error": "El contenido debe ser JSON"}), 400

    data = request.get_json()

    # 2. Validar que existan las claves necesarias
    campos_requeridos = ["base", "altura", "lado1", "lado2"]
    for campo in campos_requeridos:
        if campo not in data:
            return jsonify({"error": f"Falta el campo '{campo}' en el JSON"}), 400

    try:
        # 3. Convertir a float
        base = float(data["base"])
        altura = float(data["altura"])
        lado1 = float(data["lado1"])
        lado2 = float(data["lado2"])

        # 4. Validaciones simples (opcional)
        if base <= 0 or altura <= 0 or lado1 <= 0 or lado2 <= 0:
            return jsonify({"error": "Todos los valores deben ser mayores que cero"}), 400

        # 5. Llamar al modelo
        area, perimetro = calcular_triangulo(base, altura, lado1, lado2)

        # 6. Responder en formato JSON
        respuesta = {
            "base": base,
            "altura": altura,
            "lado1": lado1,
            "lado2": lado2,
            "area": area,
            "perimetro": perimetro
        }
        return jsonify(respuesta), 200

    except ValueError:
        return jsonify({"error": "Todos los valores deben ser numéricos"}), 400


# Endpoint de prueba simple (GET)
@app.route("/api/triangulo/ejemplo", methods=["GET"])
def ejemplo():

    # Responder con un ejemplo de JSON
    ejemplo_data = {
        "mensaje": "API de triángulo funcionando",
        "ejemplo_body": {
            "base": 10,
            "altura": 5,
            "lado1": 7,
            "lado2": 8
        }
    }
    return jsonify(ejemplo_data), 200


if __name__ == "__main__":
    app.run()