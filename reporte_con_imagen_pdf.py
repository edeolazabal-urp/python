import io

import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Image, Paragraph, SimpleDocTemplate, Spacer


def generar_grafico():
    # Datos para el gráfico de barras
    categorias = ['A', 'B', 'C', 'D']
    valores = [10, 20, 15, 25]

    # Generar el gráfico de barras
    plt.bar(categorias, valores)
    plt.xlabel('Categorías')
    plt.ylabel('Valores')
    plt.title('Gráfico de Barras')

    # Convertir el gráfico a un formato compatible con ReportLab
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    
    # Limpiar la figura de Matplotlib
    plt.clf()

    return buffer

def generar_reporte_con_imagen():
    # Crear un documento PDF
    doc = SimpleDocTemplate("reporte_con_imagen.pdf", pagesize=letter)
    
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
    contenido.append(Paragraph("Certificado", estilo_titulo))
    contenido.append(Spacer(1, 12))
    
    # Texto descriptivo
    texto = """
    La Universidad Ricardo Palma certifica que el alumno 
    """
    contenido.append(Paragraph(texto, estilo_normal))
    contenido.append(Spacer(1, 12))
    texto = """
    Edgard De Olazabal Leon 
    """
    contenido.append(Paragraph(texto, estilo_titulo2))
    contenido.append(Spacer(1, 12))
    texto = """
    Ha completado con exito el curso Python de 48 horas de duración
    """
    contenido.append(Paragraph(texto, estilo_normal))
    contenido.append(Spacer(1, 12))
    
    # Agregar imagen
    imagen = "python-imagen.jpg"  # Ruta de la imagen
    imagen_obj = Image(imagen, width=300, height=200)
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
    buffer = generar_grafico()
    
    # Convertir la imagen de bytes a Image de ReportLab
    imagen = Image(buffer, width=6*inch, height=4*inch)

    # Agregar el gráfico al contenido del reporte
    contenido.append(imagen)
    
    # Compilar el reporte
    doc.build(contenido)

if __name__ == "__main__":
    generar_reporte_con_imagen()
    
