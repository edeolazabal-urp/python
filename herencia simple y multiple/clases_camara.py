'''
Herencia simple y múltiple: Cámaras
Fecha: 10/10/2024
'''
class Camara:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def tomar_foto(self):
        print ('imprimió una foto')
    
class CamaraDigital(Camara):
    def __init__(self, largo, ancho, capacidad):
        Camara.__init__(self, largo, ancho)
        self.capacidad = capacidad
        
    def tomar_video(self):
        retorno = False
        print ('grabó un video')
        retorno = True
        return retorno
    
class CamaraAnalogica(Camara):
    def __init__(self, largo, ancho, nro_tomas):
        super().__init__(largo, ancho)
        self.nro_tomas = nro_tomas
    
    def revelar(self):
        print ('terminó de revelar las fotos')