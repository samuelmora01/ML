# Controlador principal de la aplicación Flask
# Maneja rutas y lógica de interacción con el usuario
# Autor: AperezN

# Importaciones necesarias
from flask import Flask, render_template, request
from models.triangulo import calcular_triangulo

# Inicialización de la aplicación Flask
app = Flask(__name__)

# Ruta principal que maneja el formulario y muestra resultados
@app.route('/', methods=['GET', 'POST'])
def formulario_triangulo():
    resultado = None
    error = None

    # Métodos HTTP:
    # GET  -> Mostrar formulario vacío
    # POST -> Procesar datos enviados por el usuario
    if request.method == 'POST':
        try:
            # Envío y recepción de datos desde el formulario
            base = float(request.form['base'])
            altura = float(request.form['altura'])
            lado1 = float(request.form['lado1'])
            lado2 = float(request.form['lado2'])

            area, perimetro = calcular_triangulo(base, altura, lado1, lado2)

            resultado = {
                "base": base,
                "altura": altura,
                "lado1": lado1,
                "lado2": lado2,
                "area": area,
                "perimetro": perimetro
            }
        except ValueError:
            error = "Por favor ingresa solo números válidos."

    # Plantilla HTML con Jinja2 (Vista)
    return render_template('triangulo.html',
                           resultado=resultado,
                           error=error)
    
# Ejecución de la aplicación Flask
if __name__ == '__main__':
    app.run()