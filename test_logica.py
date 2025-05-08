# test_logica.py
import unittest
from logica import comparar_jugada

class TestCompararJugada(unittest.TestCase):

    def test_piedra_vs_tijera(self):
        self.assertEqual(comparar_jugada("piedra", "tijera"), 1)

    def test_piedra_vs_papel(self):
        self.assertEqual(comparar_jugada("piedra", "papel"), -1)

    def test_piedra_vs_piedra(self):
        self.assertEqual(comparar_jugada("piedra", "piedra"), 0)

    def test_papel_vs_piedra(self):
        self.assertEqual(comparar_jugada("papel", "piedra"), 1)

    def test_papel_vs_tijera(self):
        self.assertEqual(comparar_jugada("papel", "tijera"), -1)

    def test_papel_vs_papel(self):
        self.assertEqual(comparar_jugada("papel", "papel"), 0)

    def test_tijera_vs_papel(self):
        self.assertEqual(comparar_jugada("tijera", "papel"), 1)

    def test_tijera_vs_piedra(self):
        self.assertEqual(comparar_jugada("tijera", "piedra"), -1)

    def test_tijera_vs_tijera(self):
        self.assertEqual(comparar_jugada("tijera", "tijera"), 0)

if __name__ == "__main__":
    unittest.main()
