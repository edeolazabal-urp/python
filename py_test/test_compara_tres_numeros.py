import unittest
from compara_tres_numeros import asignar_mayor, asignar_menor, asignar_medio, crear_lista, crear_lista_ordenada  

class TestCompara(unittest.TestCase):
    a = 10
    b = 30
    c = 20
    def test_encuentra_el_mayor(self):
        self.assertEqual(asignar_mayor(self.a, self.b, self.c), 30)
    def test_encuentra_el_menor(self):
        self.assertEqual(asignar_menor(self.a, self.b, self.c), 10)
    def test_encuentra_el_medio(self):
        self.assertEqual(asignar_medio(self.a, self.b, self.c), 20)
    def test_compara_lista_creada(self):
        self.assertEqual(crear_lista(self.a, self.b, self.c), [10, 20, 30])
    def test_compara_lista_ordenada(self):
        self.assertEqual(crear_lista_ordenada(self.a, self.b, self.c), [10, 20, 30])        
if __name__ == '__main__':
    unittest.main() 