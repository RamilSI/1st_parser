import json
import os
import pandas as pd
import numpy as np


# считываем данные json файла в переменную data_json
with open('parsing_catalog_imf/json_file/index2.json') as f:
    data_json_1 = json.load(f)


with open('parsing_catalog_imf/json_file/index2_2.json') as f:
    data_json_2 = json.load(f)


print(len(data_json_2),'n',len(data_json_1))