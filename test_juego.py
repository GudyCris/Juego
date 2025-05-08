import unittest
from juego import comparar_jugada  # Asegúrate de importar correctamente la función

class TestJuego(unittest.TestCase):
    
    def test_piedra_vs_tijera(self):
        self.assertEqual(comparar_jugada("piedra", "tijera"), 1)
    
    def test_tijera_vs_piedra(self):
        self.assertEqual(comparar_jugada("tijera", "piedra"), -1)
    
    def test_piedra_vs_piedra(self):
        self.assertEqual(comparar_jugada("piedra", "piedra"), 0)
    
    def test_papel_vs_tijera(self):
        self.assertEqual(comparar_jugada("papel", "tijera"), -1)
    
    def test_tijera_vs_papel(self):
        self.assertEqual(comparar_jugada("tijera", "papel"), 1)
    
    def test_papel_vs_piedra(self):
        self.assertEqual(comparar_jugada("papel", "piedra"), 1)
    
    def test_piedra_vs_papel(self):
        self.assertEqual(comparar_jugada("piedra", "papel"), -1)
    
    def test_tijera_vs_tijera(self):
        self.assertEqual(comparar_jugada("tijera", "tijera"), 0)
    
    def test_papel_vs_papel(self):
        self.assertEqual(comparar_jugada("papel", "papel"), 0)
    
    def test_piedra_vs_tijera_2(self):
        # Puedes agregar pruebas repetidas si quieres, por ejemplo:
        self.assertEqual(comparar_jugada("piedra", "tijera"), 1)

if __name__ == '__main__':
    unittest.main()
