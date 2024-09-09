import pandas as pd
import matplotlib.pyplot as plt

def calcular_frequencias(tabela: pd.Series) -> pd.DataFrame:
    return tabela.value_counts().sort_index()

def calcular_frequencias_relativas(tabela: pd.Series) -> pd.DataFrame:
    return tabela.value_counts(normalize=True).sort_index() * 100

def calcular_proporcao(tabela: pd.Series, condicao) -> float:
    return tabela[condicao(tabela)].shape[0] / tabela.shape[0]

def calcular_media(tabela: pd.Series) -> float:
    return tabela.mean()

def calcular_mediana(tabela: pd.Series) -> float:
    return tabela.median()

def calcular_moda(tabela: pd.Series) -> pd.Series:
    return tabela.mode()

def calcular_variancia(tabela: pd.Series) -> float:
    return tabela.var()

def calcular_desvio_padrao(tabela: pd.Series) -> float:
    return tabela.std()

def gerar_tabela_classes(tabela: pd.Series, num_classes: int) -> pd.DataFrame:
    intervalos = pd.cut(tabela, bins=num_classes)
    frequencias = intervalos.value_counts().sort_index()
    return pd.DataFrame({'Classe': frequencias.index, 'Frequência': frequencias.values})

def desenhar_histograma(tabela: pd.Series, titulo: str = "Histograma de Frequências Relativas"):
    frequencias_relativas = tabela.value_counts(normalize=True).sort_index() * 100
    plt.figure(figsize=(8,6))
    frequencias_relativas.plot(kind='bar', color='skyblue')
    plt.title(titulo)
    plt.xlabel('Valores')
    plt.ylabel('Frequência Relativa (%)')
    plt.show()

def calcular_media_ponderada(tabela: pd.DataFrame, coluna_classes: str, coluna_frequencias: str) -> float:
    return (tabela[coluna_classes] * tabela[coluna_frequencias]).sum() / tabela[coluna_frequencias].sum()

def calcular_variancia_ponderada(tabela: pd.DataFrame, coluna_classes: str, coluna_frequencias: str, media_ponderada: float) -> float:
    return ((tabela[coluna_classes] - media_ponderada)**2 * tabela[coluna_frequencias]).sum() / tabela[coluna_frequencias].sum()

def calcular_desvio_padrao_ponderado(tabela: pd.DataFrame, coluna_classes: str, coluna_frequencias: str, media_ponderada: float) -> float:
    variancia_ponderada = calcular_variancia_ponderada(tabela, coluna_classes, coluna_frequencias, media_ponderada)
    return variancia_ponderada ** 0.5
