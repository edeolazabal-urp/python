from clases_vehiculo import Vehiculo, VehiculoAereo, VehiculoTerrestre
from clases_camara import Camara, CamaraAnalogica, CamaraDigital

class DronDigital(VehiculoAereo, CamaraDigital):
    def __init__(self, velocidad_maxima=None, largo=None, ancho=NotImplementedError, capacidad=None, altura_minima=None):
        VehiculoAereo.__init__(self, velocidad_maxima)
        CamaraDigital.__init__(self, largo, ancho, capacidad)
        self.altura_minima = altura_minima
        
    def tomar_video(self):
        print ('capturó video') 
        
class DronAnalogico(VehiculoAereo, CamaraAnalogica):
    def __init__(self, velocidad_maxima=None, largo=None, ancho=NotImplementedError, nro_tomas=None, altura_maxima=None):
        VehiculoAereo.__init__(self, velocidad_maxima)
        CamaraAnalogica.__init__(self, largo, ancho, nro_tomas)
        self.altura_maxima = altura_maxima
        
class AutoCamaraDigital(VehiculoTerrestre, CamaraDigital):
    def __init__(self, velocidad_maxima=None, largo=None, ancho=NotImplementedError, capacidad=None, duracion_maxima=None):
        VehiculoTerrestre.__init__(self, velocidad_maxima)
        CamaraDigital.__init__(self, largo, ancho, capacidad)
        self.duracion_maxima = duracion_maxima
        
    def reproducir_video(self):
        print ('proyectó el video')
        
class AutoCamaraAnalogica(VehiculoTerrestre, CamaraAnalogica):
    def __init__(self, velocidad_maxima=None, largo=None, ancho=NotImplementedError, nro_tomas=None, ubicacion=None):
        VehiculoTerrestre.__init__(self, velocidad_maxima)
        CamaraAnalogica.__init__(self, largo, ancho, nro_tomas)
        self.ubicacion = ubicacion
        
import unittest

class Test(unittest.TestCase):
    def test_1(self):
        d = DronDigital(100, 10, 5, 100, 50)
        self.assertEqual(d.velocidad_maxima, 100)
        self.assertEqual(d.largo, 10)
        self.assertEqual(d.ancho, 5)
        self.assertEqual(d.capacidad, 100)
        self.assertEqual(d.altura_minima, 50)
        self.assertEqual(d.tomar_video(), None)
    
    def test_2(self):
        d = DronAnalogico(100, 10, 5, 100, 50)
        self.assertEqual(d.velocidad_maxima, 100)
        self.assertEqual(d.largo, 10)
        self.assertEqual(d.ancho, 5)
        self.assertEqual(d.nro_tomas, 100)
        self.assertEqual(d.altura_maxima, 50)
        self.assertEqual(d.revelar(), None)
           
    def test_3(self):
        a = AutoCamaraDigital(100, 10, 5, 100, 50)
        self.assertEqual(a.velocidad_maxima, 100)
        self.assertEqual(a.largo, 10)
        self.assertEqual(a.ancho, 5)
        self.assertEqual(a.capacidad, 100)
        self.assertEqual(a.duracion_maxima, 50)
        self.assertEqual(a.reproducir_video(), None)
        
    def test_4(self):
        a = AutoCamaraAnalogica(100, 10, 5, 100, 50)
        self.assertEqual(a.velocidad_maxima, 100)
        self.assertEqual(a.largo, 10)
        self.assertEqual(a.ancho, 5)
        self.assertEqual(a.nro_tomas, 100)
        self.assertEqual(a.ubicacion, 50)
        self.assertEqual(a.revelar(), None)

if __name__ == '__main__':
    unittest.main()