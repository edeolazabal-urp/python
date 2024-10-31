'''
Pruebas unitarias con unittest
'''
import unittest
from clases_camara import Camara, CamaraDigital, CamaraAnalogica

class Pruebas(unittest.TestCase):
    def test_camara(self):
        c = Camara()
        c.largo = 10
        c.ancho = 5
        self.assertEqual(c.largo, 10)

        
    def test_camara_digital(self):
        cd = CamaraDigital()
        cd.largo = 11
        cd.ancho= 6
        cd.capacidad = 100
        self.assertEqual(cd.capacidad, 100)
        self.assertGreater(cd.largo, 5)
        self.assertTrue(cd.tomar_video())
    
    def test_camara_analogica(self):
        ca = CamaraAnalogica()
        ca.largo = 12
        ca.ancho = 7
        ca.nro_tomas = 36
        self.assertEqual(ca.nro_tomas, 36)
        self.assertLess(ca.ancho, 10)
        self.assertIsNone(ca.revelar())
        