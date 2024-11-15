#Función para gráfico de barras
import matplotlib.pyplot as plt

def barplot(df, xlabel, ylabel, titulo):
    df_grouped = df.groupby(xlabel)[ylabel].mean().reset_index()

    categorias = df_grouped[xlabel]
    valores = df_grouped[ylabel]

    plt.figure(figsize=(7, 4))
    plt.bar(categorias, valores, color='skyblue', edgecolor='black')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(titulo)
    plt.show()