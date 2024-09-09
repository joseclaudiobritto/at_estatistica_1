import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from metodos import gerar_tabela_classes

medidas_pecas = [102.8, 136.4, 110.1, 115.9, 118.5, 149.3, 125.3, 144.8, 129.7, 132.7,
                 135.0, 108.2, 138.1, 138.6, 139.6, 144.4, 125.9, 145.2, 145.7, 120.4]

tabela_classes_pecas = gerar_tabela_classes(pd.Series(medidas_pecas), num_classes=5)
print(tabela_classes_pecas)
