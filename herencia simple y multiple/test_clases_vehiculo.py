'''
Pruebas unitarias de vehiculo
'''
import unittest
from clases_vehiculo import Vehiculo, VehiculoAereo, VehiculoTerrestre

class VerificarVehiculos(unittest.TestCase):
    def test_vehiculo_sin_proporcionar_velocidad_maxima(self):
        v = Vehiculo()
        self.assertEqual(v.velocidad_maxima,75)
        
    def test_vehiculo_con_velocidad_maxima(self):
        v = Vehiculo(180)
        self.assertEqual(v.velocidad_maxima,180)
        
    def test_vehiculo_modifica_velocidad_maxima(self):
        v = Vehiculo()
        v.velocidad_maxima = 50
        self.assertEqual(v.velocidad_maxima,50)
    
    def test_verificar_metodos_vehiculo(self):
        v = Vehiculo()
        self.assertIsNone(v.avanzar())
        self.assertIsNone(v.detener())
        
    def test_vehiculo_aereo(self):
        va = VehiculoAereo(300)
        self.assertEqual(va.velocidad_maxima,300)
        self.assertIsNone(va.avanzar())
        self.assertIsNone(va.detener())
        self.assertIsNone(va.volar())
        
    def test_vehiculo_terrestre(self):
        vt = VehiculoTerrestre()
        vt.velocidad_maxima = 175
        self.assertEqual(vt.velocidad_maxima,175)
        self.assertIsNone(vt.avanzar())
        self.assertIsNone(vt.detener())
        self.assertIsNone(vt.retroceder())
