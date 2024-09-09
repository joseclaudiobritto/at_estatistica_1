import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from metodos import calcular_media_ponderada, calcular_mediana, calcular_moda

comodos_classe = [2, 3, 4, 5, 6, 7]
fi_comodos = [4, 7, 5, 2, 1, 1]

df_comodos = pd.DataFrame({
    'Comodos': comodos_classe,
    'fi': fi_comodos
})

print("Tabela de cômodos:")
print(df_comodos)

media_comodos = calcular_media_ponderada(df_comodos, 'Comodos', 'fi')
print("\nMédia dos cômodos:")
print(media_comodos)

mediana_comodos = calcular_mediana(pd.Series(comodos_classe).repeat(fi_comodos))
print("\nMediana dos cômodos:")
print(mediana_comodos)

moda_comodos = calcular_moda(pd.Series(comodos_classe).repeat(fi_comodos))
print("\nModa dos cômodos:")
print(moda_comodos)
