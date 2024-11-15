
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
import pandas as pd
import joblib

#Función para gráfico de barras
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
    
# Histograma y boxplot


def plot_hist_box(df, list_numericas):

    color = 'lightblue'
    
    for var in list_numericas:
        # Filtrar nulos para evitar errores en los gráficos
        df_var = df.dropna(subset=[var])
        
        # Crear gráficos
        fig, axs = plt.subplots(1, 2, figsize=(12, 6))
        
        # Histograma
        sns.histplot(df_var[var], kde=False, color=color, bins=10, ax=axs[0])
        axs[0].set_title(f'Histograma de {var}')
        axs[0].set_xlabel(var)
        axs[0].set_ylabel('Frecuencia')
        
        # Boxplot
        sns.boxplot(x=df_var[var], color=color, ax=axs[1])
        axs[1].set_title(f'Boxplot de {var}')
        axs[1].set_xlabel(var)
        
        plt.tight_layout()
        plt.show()

#Procesamiento de las bases de datos
def procesar_datos(df, scaler=None):
    
    df_dummizado = pd.get_dummies(df, columns=['HomeOwnership', 'Education', 'MaritalStatus'], dtype=int)
    
    if scaler is None:
        scaler = MinMaxScaler()
        df_scaled = pd.DataFrame(scaler.fit_transform(df_dummizado), columns=df_dummizado.columns)
    else:
        df_scaled = pd.DataFrame(scaler.transform(df_dummizado), columns=df_dummizado.columns)
    
    return df_scaled, scaler