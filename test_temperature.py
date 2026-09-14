"""Pruebas unitarias para reglas de conversión sin servidor web."""

import unittest

from temperature import convert, normalize_unit


class TemperatureConversionTest(unittest.TestCase):
    def test_converts_celsius_to_fahrenheit(self):
        self.assertEqual(convert(25, "celsius", "fahrenheit"), 77)

    def test_converts_fahrenheit_to_kelvin(self):
        self.assertAlmostEqual(convert(32, "fahrenheit", "kelvin"), 273.15)

    def test_converts_kelvin_to_celsius(self):
        self.assertAlmostEqual(convert(273.15, "kelvin", "celsius"), 0)

    def test_normalizes_aliases(self):
        self.assertEqual(normalize_unit(" F "), "fahrenheit")
        self.assertEqual(normalize_unit("centigrade"), "celsius")

    def test_rejects_unknown_units(self):
        self.assertIsNone(normalize_unit("rankine"))
        self.assertIsNone(normalize_unit(None))


if __name__ == "__main__":
    unittest.main()
