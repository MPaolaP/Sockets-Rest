"""Reglas puras de conversión de temperatura reutilizables y comprobables."""

from __future__ import annotations

from typing import Any

UNITS = {
    "celsius": {"symbol": "°C", "aliases": {"c", "celsius", "centigrade"}},
    "fahrenheit": {"symbol": "°F", "aliases": {"f", "fahrenheit"}},
    "kelvin": {"symbol": "K", "aliases": {"k", "kelvin"}},
}


def normalize_unit(unit: Any) -> str | None:
    """Convierte un alias de unidad a su nombre canónico."""
    if not isinstance(unit, str):
        return None
    candidate = unit.strip().lower()
    for canonical, details in UNITS.items():
        if candidate in details["aliases"]:
            return canonical
    return None


def convert(value: float, source_unit: str, target_unit: str) -> float:
    """Convierte *value* entre Celsius, Fahrenheit y Kelvin."""
    if source_unit == "celsius":
        celsius = value
    elif source_unit == "fahrenheit":
        celsius = (value - 32) * 5 / 9
    else:
        celsius = value - 273.15

    if target_unit == "celsius":
        return celsius
    if target_unit == "fahrenheit":
        return (celsius * 9 / 5) + 32
    return celsius + 273.15
