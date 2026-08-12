import unittest 
from math_utils import es_par #aún no existe (RED)

class TestEsPar (unittest.TestCase):
    def test_4_es_par(self):
        self.assertTrue(es_par(4))

    def test_negativo_par(self):
        self.assertTrue(es_par(-8))

    def test_negativo_impar(self):
        self.assertFalse(es_par(-3))

    def test_0_es_par(self):
        self.assertTrue(es_par(0))

    def test_15_es_impar(self):
        self.assertFalse(es_par(15))

if __name__ == "__main__":
    unittest.main()