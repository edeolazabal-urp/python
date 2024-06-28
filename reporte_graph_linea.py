import datetime
from collections import defaultdict

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer

import rutina_graficos as rutina


def archivo_a_arreglo(nombre_archivo):
    datos, categorias, valores = [], [], []
    # Crear un diccionario para almacenar la suma de importes por mes
    with open(nombre_archivo, 'r') as archivo:
        encabezado = archivo.readline() # Leer la primera línea (encabezado
        for linea in archivo:
            dato = linea.strip('\n').split(';')
            datos.append((dato[1], int(dato[2])))
    
    importes_por_mes = defaultdict(int)

    # Filtrar y sumar los importes válidos por mes
    for mes, importe in datos:
        if 0 <= importe < 1000:
            importes_por_mes[mes] += importe

    # Convertir el diccionario en una lista de tuplas (mes, suma_importes)
    categorias = list(importes_por_mes.keys())
    valores = list(importes_por_mes.values())

    return categorias, valores    

def generar_reporte_con_imagen(nombre, categorias, valores, tipo_grafico):
    # Crear un documento PDF
    fecha = datetime.datetime.now().strftime("%d-%m-%Y_%H%M%S")

    #fecha = str(datetime.now().strftime("%d-%m-%Y_%H%M%S"))
    doc = SimpleDocTemplate(f"{nombre}_{fecha}.pdf", pagesize=letter)
    
    # Estilos para el texto
    estilos = getSampleStyleSheet()
    estilo_normal = estilos["Normal"]
    ## estilo_titulo = estilos["Heading1"]
    
    # Estilo para el título (con alineación centrada)
    ##  estilo_titulo = ParagraphStyle(name='TitleStyle', alignment=1, fontSize=20, bold=True, spaceAfter=12)
    estilo_titulo = ParagraphStyle(name='Heading', alignment=1, fontSize=20, bold=True, spaceAfter=12)
   
    estilo_titulo2 = estilos["Heading2"]
    
    # Contenido del reporte (texto e imagen)
    contenido = []
    
    # Título
    contenido.append(Paragraph(nombre, estilo_titulo))
    contenido.append(Spacer(1, 12))
    
    # Texto descriptivo
    texto = """
    Se presenta el gráfico de barras con las categorías y valores correspondientes.
    """
    contenido.append(Paragraph(texto, estilo_normal))
    contenido.append(Spacer(1, 12))
    
    # Agregar imagen
    imagen = "urp.jpg"  # Ruta de la imagen
    imagen_obj = Image(imagen, width=150, height=150)
    contenido.append(imagen_obj)
    
    contenido.append(Spacer(1, 12))
    '''
    # Generar el gráfico y convertirlo a formato compatible con ReportLab
    buffer = generar_grafico()
    # Agregar el gráfico al contenido del reporte
    imagen_obj = buffer.getvalue()
    contenido.append(imagen_obj)
    '''
    
    # Generar el gráfico y convertirlo a formato compatible con ReportLab
    buffer = rutina.generar_grafico(categorias, valores, tipo_grafico)
    
    # Convertir la imagen de bytes a Image de ReportLab
    imagen = Image(buffer, width=6*inch, height=4*inch)

    # Agregar el gráfico al contenido del reporte
    contenido.append(imagen)
    
    # Compilar el reporte
    doc.build(contenido)

if __name__ == "__main__":
    categorias, valores = archivo_a_arreglo('gastos.csv')
    generar_reporte_con_imagen('Reporte de Gastos', categorias, valores, 'pie')