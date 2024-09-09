import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from metodos import calcular_desvio_padrao_ponderado, calcular_media_ponderada, calcular_variancia_ponderada

comodos_classe = [2, 3, 4, 5, 6, 7]
fi_comodos = [4, 7, 5, 2, 1, 1]

df_comodos_variancia = pd.DataFrame({
    'Comodos': comodos_classe,
    'fi': fi_comodos
})

print("Tabela de cômodos:")
print(df_comodos_variancia)

media_ponderada_comodos = calcular_media_ponderada(df_comodos_variancia, 'Comodos', 'fi')
print("\nMédia ponderada dos cômodos:")
print(media_ponderada_comodos)

variancia_comodos = calcular_variancia_ponderada(df_comodos_variancia, 'Comodos', 'fi', media_ponderada_comodos)
print("\nVariância ponderada dos cômodos:")
print(variancia_comodos)

desvio_padrao_comodos = calcular_desvio_padrao_ponderado(df_comodos_variancia, 'Comodos', 'fi', media_ponderada_comodos)
print("\nDesvio padrão ponderado dos cômodos:")
print(desvio_padrao_comodos)