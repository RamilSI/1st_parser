import json
import os
import pandas as pd
import numpy as np




df = pd.read_csv('parsing_catalog_imf/csv_files/my7_1.csv')
print(df['products_title'][220][230])



# df['editions_img'].replace('', np.nan, inplace=True)
# df.dropna(subset=['editions_img'], inplace=True)
# df['editions_Цвет'] = df['editions_Цвет'].fillna('бесцветный')
# for i,e in enumerate (df['editions_Цвет']):
#   if '/' in e:
#     df['editions_Цвет'][i] = e.replace('/','-')
# df['products_title'][221] = df['products_title'][221].replace('/','-')
#
# #print(df)
#
# df.to_csv('parsing_catalog_imf/csv_files/my7_1.csv', index=False)