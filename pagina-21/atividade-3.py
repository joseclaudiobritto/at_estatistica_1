import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from metodos import calcular_media_ponderada

limite_inferior = [102.8, 112.8, 122.8, 132.8, 142.8]
limite_superior = [112.8, 122.8, 132.8, 142.8, 152.8]

fi = [3, 3, 4, 5, 5]

pmi = [(li + ls) / 2 for li, ls in zip(limite_inferior, limite_superior)]

df_dimensoes = pd.DataFrame({
    'Intervalo de Classes': [f"{li} - {ls}" for li, ls in zip(limite_inferior, limite_superior)],
    'fi': fi,
    'Pmi': pmi
})

df_dimensoes['Pmi * fi'] = df_dimensoes['Pmi'] * df_dimensoes['fi']

print("Tabela de dimensões:")
print(df_dimensoes)

media_ponderada_dimensoes = calcular_media_ponderada(df_dimensoes, 'Pmi', 'fi')

print("\nMédia ponderada das dimensões:")
print(media_ponderada_dimensoes)
