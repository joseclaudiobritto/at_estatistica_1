import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from metodos import calcular_media_ponderada, calcular_mediana, calcular_moda

notas_classe = [1.0, 2.3, 3.6, 4.9, 6.2, 7.5, 8.8, 10.1]
fi_notas = [8, 10, 7, 6, 2, 4, 13, 4]

df_notas = pd.DataFrame({
    'Notas': notas_classe,
    'fi': fi_notas
})

print("Tabela de notas:")
print(df_notas)

media_notas = calcular_media_ponderada(df_notas, 'Notas', 'fi')
print("\nMédia:")
print(media_notas)

mediana_notas = calcular_mediana(pd.Series(notas_classe).repeat(fi_notas))
print("\nMediana das notas:")
print(mediana_notas)

moda_notas = calcular_moda(pd.Series(notas_classe).repeat(fi_notas))
print("\nModa das notas:")
print(moda_notas)
