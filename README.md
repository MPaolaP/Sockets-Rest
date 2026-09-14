# 🌡️ Temperature Converter API

Una API REST clara, rápida y lista para enseñar o usar como punto de partida. Convierte temperaturas entre **Celsius**, **Fahrenheit** y **Kelvin** usando peticiones `GET` o `POST`, con validación, respuestas JSON consistentes y pruebas incluidas.

## Características

- ✨ Conversión entre las tres escalas de temperatura más usadas.
- 🔁 Soporte para `GET` (ideal para explorar) y `POST` con JSON (ideal para integraciones).
- 🛡️ Validación de datos, alias de unidades (`c`, `f`, `k`) y errores legibles.
- ❤️ Endpoint de salud para comprobar rápidamente que el servicio está activo.
- 🧪 Pruebas unitarias de las reglas de conversión sin dependencias adicionales.

## Inicio rápido

> Requiere Python 3.10 o superior.

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
python rest.py
```

El servidor queda disponible en `http://127.0.0.1:5000`.

## Endpoints

| Método | Ruta | Descripción |
| --- | --- | --- |
| `GET` | `/` | Presentación y rutas disponibles. |
| `GET` | `/health` | Estado del servicio y fecha UTC. |
| `GET` | `/units` | Unidades admitidas. |
| `GET` / `POST` | `/convert` | Convierte una temperatura. |

### Convertir con GET

```bash
curl "http://127.0.0.1:5000/convert?temperature=25&unit=celsius&target_unit=fahrenheit"
```

```json
{
  "conversion": {
    "input": {"value": 25.0, "unit": "celsius", "symbol": "°C"},
    "output": {"value": 77.0, "unit": "fahrenheit", "symbol": "°F"}
  },
  "meta": {"rounded_to": 2}
}
```

`unit` y `target_unit` aceptan `celsius`/`c`, `fahrenheit`/`f` y `kelvin`/`k`. Si se omiten, la API convierte de Celsius a Fahrenheit.

### Convertir con POST

```bash
curl -X POST http://127.0.0.1:5000/convert \
  -H "Content-Type: application/json" \
  -d '{"temperature": 32, "unit": "f", "target_unit": "kelvin"}'
```

## Errores

Las solicitudes inválidas responden con el código HTTP apropiado y un formato uniforme:

```json
{
  "error": {
    "message": "'temperature' debe ser un número.",
    "status": 400
  }
}
```

## Pruebas

```bash
python -m unittest -v
```

## Otros ejemplos del repositorio

- `Ejemplo.py`: servidor TCP de eco básico.
- `Imagen.py`: receptor TCP que guarda una imagen como `imagen_recibida.jpg`.

Ambos usan el puerto `65432`; ejecútalos de uno en uno.
