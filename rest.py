"""API REST pequeña y completa para convertir temperaturas.

Se puede ejecutar directamente con ``python rest.py`` o importar ``app`` desde
un servidor WSGI. El módulo no depende de extensiones de Flask para que sea
fácil de probar y de usar como ejemplo educativo.
"""

from __future__ import annotations

from datetime import UTC, datetime
from http import HTTPStatus
from math import isfinite
from typing import Any

from flask import Flask, jsonify, request
from temperature import UNITS, convert, normalize_unit

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

def api_error(message: str, status: HTTPStatus = HTTPStatus.BAD_REQUEST):
    """Devuelve errores con un formato estable para consumidores de la API."""
    return jsonify({"error": {"message": message, "status": status.value}}), status.value


def conversion_response(value: Any, unit: Any, target_unit: Any):
    """Valida la entrada y crea la respuesta de una conversión."""
    try:
        temperature = float(value)
    except (TypeError, ValueError):
        return api_error("'temperature' debe ser un número.")
    if not isfinite(temperature):
        return api_error("'temperature' debe ser un número finito.")

    source = normalize_unit(unit)
    target = normalize_unit(target_unit)
    if not source or not target:
        return api_error("Las unidades válidas son: celsius, fahrenheit y kelvin.")
    if convert(temperature, source, "kelvin") < 0:
        return api_error("La temperatura no puede estar por debajo del cero absoluto.")

    result = round(convert(temperature, source, target), 2)
    return jsonify(
        {
            "conversion": {
                "input": {"value": temperature, "unit": source, "symbol": UNITS[source]["symbol"]},
                "output": {"value": result, "unit": target, "symbol": UNITS[target]["symbol"]},
            },
            "meta": {"rounded_to": 2},
        }
    )


@app.get("/")
def index():
    """Presenta los enlaces principales de la API."""
    return jsonify(
        {
            "name": "Temperature Converter API",
            "version": "1.0.0",
            "endpoints": {"health": "/health", "units": "/units", "convert": "/convert"},
        }
    )


@app.get("/health")
def health():
    return jsonify({"status": "ok", "timestamp": datetime.now(UTC).isoformat()})


@app.get("/units")
def units():
    return jsonify({"units": [{"name": name, "symbol": data["symbol"]} for name, data in UNITS.items()]})


@app.route("/convert", methods=["GET", "POST"])
def convert_temperature():
    """Convierte desde parámetros query (GET) o JSON (POST)."""
    payload = request.args if request.method == "GET" else request.get_json(silent=True)
    if not payload:
        return api_error("Envía temperature, unit y target_unit en la solicitud.")
    return conversion_response(
        payload.get("temperature"), payload.get("unit", "celsius"), payload.get("target_unit", "fahrenheit")
    )


@app.errorhandler(404)
def not_found(_error):
    return api_error("Ruta no encontrada.", HTTPStatus.NOT_FOUND)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
