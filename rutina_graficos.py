import io

import matplotlib.pyplot as plt


def generar_grafico(categorias, valores, tipo_grafico):

    colores = ['ligthgreen', 'purple', 'orange', 'deeppink', 'skyblue', 'lightcoral', 'blue', 'red', 'green']
    match (tipo_grafico):
        case 'linea':
            plt.plot(categorias, valores, marker='o', color='green', linestyle='-')
            # Agregar los valores encima de cada punto
            for i, valor in enumerate(valores):
                plt.annotate(str(valor), (categorias[i], valor), textcoords="offset points", xytext=(0,10), ha='center')
        case 'barra':
            items = plt.bar(categorias, valores, color=colores)  #'lightgreen')
             # Agregar los valores encima de cada barra 
            for item in items:
                yval = item.get_height()
                plt.text(item.get_x() + item.get_width() / 2, yval + 10, int(yval), ha='center', va='bottom')
        case 'area':
            plt.figure(figsize=(10, 5))
            plt.fill_between(categorias, valores, color='lightgreen', alpha=0.4)

            # Agregar los valores encima de cada área
            for i, valor in enumerate(valores):
                plt.text(i, valor + 20, str(valor), ha='center')
        case 'pie':
            # Crear el gráfico circular (gráfico de pastel)
            plt.figure(figsize=(8, 8))
            plt.pie(valores, labels=categorias, autopct='%1.1f%%', startangle=140, colors=['lightblue', 'lightgreen', 'lightcoral', 'lightskyblue', 'lightpink'])

            # Agregar los valores encima de cada porción
            for i, valor in enumerate(valores):
                plt.text(i, 0, str(valor), color='black', ha='center', fontsize=10)
    
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