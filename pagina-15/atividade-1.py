import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from metodos import gerar_tabela_classes

estaturas = [182, 164, 180, 186, 167, 171, 161, 180, 
             176, 174, 165, 180, 185, 172, 165, 174,
             179, 163, 177, 170, 186, 186, 186, 171, 
             160, 166, 187, 162, 163, 166, 167, 187,
             174, 169, 175, 161, 182, 183, 160, 186, 
             174, 176, 188, 169, 173, 160, 161, 183]

tabela_classes_estaturas = gerar_tabela_classes(pd.Series(estaturas), num_classes=5)
print(tabela_classes_estaturas)