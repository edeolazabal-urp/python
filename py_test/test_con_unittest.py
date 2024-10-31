import unittest

from main import suma

class TestSuma(unittest.TestCase):
    def test_suma_positivos(self):
        self.assertEqual(suma(1, 2), 3)
    
    def test_suma_negativos(self):
        self.assertEqual(suma(-1, -2), -3)
    
    def test_suma_cero(self):
        self.assertEqual(suma(0, 0), 0)
    
    def test_suma_mixto(self):
        self.assertEqual(suma(-1, 1), 0)
        
    def test_suma_mixto_mayor(self):
        self.assertGreater(suma(-1, 1), -1)
    
    def test_suma_mixto_menor(self):
        self.assertLess(suma(-1, 1), 1)
    
    def test_suma_mixto_mayor_igual(self):
        self.assertGreaterEqual(suma(-1, 1), 0)
        
    def test_suma_mixto_menor_igual(self):
        self.assertLessEqual(suma(-1, 1), 0)
        
    def test_suma_mixto_no_igual(self):
        self.assertNotEqual(suma(-1, 1), 1)
    
    def test_suma_mixto_no_es_none(self):
        self.assertIsNotNone(suma(-1, 1), NotImplemented)
        
        
    def test_suma_mixto_es_instance(self):
        self.assertIsInstance(suma(-1, 1), int)
        
    def test_suma_mixto_no_es_instance(self):
        self.assertNotIsInstance(suma(-1, 1), str)
        
    def test_suma_mixto_es(self):
        self.assertIs(suma(-1, 1), 0)
        
    def test_suma_mixto_no_es(self):
        self.assertIsNot(suma(-1, 1), 1)
    
    def test_suma_mixto_in(self):    
        self.assertLogs(suma(-1, 1), 1)
        
    def test_suma_mixto_no_in(self):    
        self.assertNotIn(suma(-1, 1), [1,2])
    
   
    def test_suma_mixto_raises_no_is(self):
        self.assertRaises(TypeError, suma(-1, 1), {0: 0})
        
            
    def test_suma_parametrizada(self):
        test_cases = [
            (1, 2, 3),
            (-1, -2, -3),
            (0, 0, 0),
            (-1, 1, 0)
        ]
        for x, y, resultado in test_cases:
            with self.subTest(x=x, y=y, resultado=resultado):
                self.assertEqual(suma(x, y), resultado)
                
if __name__ == '__main__':
    unittest.main()