# Triángulo REST — Microservicio Flask

Microservicio REST que calcula el área y perímetro de un triángulo. Diseñado como ejemplo educativo: la lógica matemática está en `models/triangulo.py` y el servicio HTTP en `app.py`.

---

## Estructura

- `app.py` — servidor Flask con el endpoint REST `/api/triangulo` y un endpoint de ejemplo `/api/triangulo/ejemplo`.
- `models/triangulo.py` — funciones del modelo:
  - `calcular_area(base, altura)`
  - `calcular_perimetro(base, lado1, lado2)`
  - `calcular_triangulo(base, altura, lado1, lado2)`
- `requirements.txt` — dependencias (`Flask`, `gunicorn`).

---

## Requisitos

- Python 3.8+ recomendado
- Virtualenv (recomendado)

Instala dependencias:

Windows PowerShell
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Linux / macOS
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Endpoints

1) POST /api/triangulo
- Descripción: calcula área y perímetro a partir de los 4 valores.
- Content-Type: `application/json`
- Body (ejemplo):
```json
{
  "base": 10,
  "altura": 5,
  "lado1": 7,
  "lado2": 8
}
```
- Respuesta (200 OK):
```json
{
  "base": 10.0,
  "altura": 5.0,
  "lado1": 7.0,
  "lado2": 8.0,
  "area": 25.0,
  "perimetro": 25.0
}
```
- Errores posibles:
  - 400: JSON incorrecto, campos faltantes o valores no numéricos/<=0.

2) GET /api/triangulo/ejemplo
- Devuelve un JSON con un ejemplo y mensaje de salud.

---

## Ejemplos de uso

Usando `curl`:

```bash
curl -X POST https://<TU_HOST>/api/triangulo \
  -H "Content-Type: application/json" \
  -d '{"base":10, "altura":5, "lado1":7, "lado2":8}'
```

Usando PowerShell (Invoke-RestMethod):

```powershell
$body = @{ base=10; altura=5; lado1=7; lado2=8 }
Invoke-RestMethod -Uri http://127.0.0.1:5000/api/triangulo -Method Post -ContentType 'application/json' -Body ($body | ConvertTo-Json)
```

---

## Ejecutar localmente

Desarrollo (debug):

```bash
python app.py
```

Producción (recomendado):

```bash
gunicorn app:app --bind 0.0.0.0:5000
```

Si despliegas en Render u otra PaaS, usa `gunicorn app:app --bind 0.0.0.0:$PORT` como start command.

---

## Autor
AperezN — material educativo / ejemplo didáctico.