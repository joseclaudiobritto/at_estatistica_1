import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from metodos import calcular_proporcao, desenhar_histograma

# Questão A
particulas = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
frequencia_particulas = pd.Series([1, 2, 3, 12, 11, 15, 18, 10, 12, 4, 5, 3, 1, 2, 1])

proporcao_ao_menos_uma = calcular_proporcao(particulas.repeat(frequencia_particulas), lambda x: x >= 1)
proporcao_ao_menos_cinco = calcular_proporcao(particulas.repeat(frequencia_particulas), lambda x: x >= 5)

print("Questão A - Proporção de partículas com pelo menos 1:")
print(proporcao_ao_menos_uma)

print("Questão A - Proporção de partículas com pelo menos 5:")
print(proporcao_ao_menos_cinco)

# Questão B
proporcao_5_10_inclusive = calcular_proporcao(particulas.repeat(frequencia_particulas), lambda x: x.between(5, 10, inclusive='both'))
proporcao_5_10_exclusivo = calcular_proporcao(particulas.repeat(frequencia_particulas), lambda x: x.between(5, 10, inclusive='neither'))

print("\nQuestão B - Proporção de partículas entre 5 e 10 (inclusivo):")
print(proporcao_5_10_inclusive)

print("Questão B - Proporção de partículas entre 5 e 10 (exclusivo):")
print(proporcao_5_10_exclusivo)

# Questão C
print("\nQuestão C - Desenho do Histograma:")
desenhar_histograma(particulas.repeat(frequencia_particulas), "Histograma de Partículas de Contaminação")


def calcular_proporcao(tabela: pd.Series, condicao) -> float:
    return tabela[condicao(tabela)].shape[0] / tabela.shape[0]
