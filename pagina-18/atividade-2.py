import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from metodos import calcular_frequencias, calcular_frequencias_relativas, calcular_proporcao, desenhar_histograma

# Questão A
transdutores = [
    2, 1, 2, 4, 0, 1, 3, 2, 0, 5, 3, 3, 1, 3, 2, 4, 7, 0, 2, 3, 
    0, 4, 2, 1, 3, 1, 1, 3, 4, 1, 2, 3, 2, 2, 8, 4, 5, 1, 3, 1, 
    5, 0, 2, 3, 2, 1, 0, 6, 4, 2, 1, 6, 0, 3, 3, 3, 6, 1, 2, 3
]

frequencias = calcular_frequencias(pd.Series(transdutores))
frequencias_relativas = calcular_frequencias_relativas(pd.Series(transdutores))

print("Questão A - Frequências:")
print(frequencias)

print("Questão A - Frequências Relativas:")
print(frequencias_relativas)


# Questão B
proporcao_max_5 = calcular_proporcao(pd.Series(transdutores), lambda x: x <= 5)
proporcao_menos_5 = calcular_proporcao(pd.Series(transdutores), lambda x: x < 5)
proporcao_min_5 = calcular_proporcao(pd.Series(transdutores), lambda x: x >= 5)

print("\nQuestão B - Proporção de valores <= 5:")
print(proporcao_max_5)

print("Questão B - Proporção de valores < 5:")
print(proporcao_menos_5)

print("Questão B - Proporção de valores >= 5:")
print(proporcao_min_5)


# Questão C
print("\nQuestão C - Desenho do Histograma:")
desenhar_histograma(pd.Series(transdutores), "Histograma de Transdutores Fora das Especificações")
