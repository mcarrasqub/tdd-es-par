import unittest 
from math_utils import es_multiplo_de #aún no existe (RED)

class TestEsMultiplo (unittest.TestCase):
     def test_4_es_multiplo_de_2(self):
        self.assertTrue(es_multiplo_de(4, 2))

     def test_8_no_es_multiplo_de_3(self):
        self.assertFalse(es_multiplo_de(8, 3))

     def test_0_es_multiplo_de_5(self):
        self.assertTrue(es_multiplo_de(0, 5))

     def test_negativo_es_multiplo_de(self):
        self.assertTrue(es_multiplo_de(-8, 4))
    
     def test_negativo_no_es_multiplo_de(self):
        self.assertFalse(es_multiplo_de(-7, 3))