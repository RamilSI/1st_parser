import json
import os
import pandas as pd
import numpy as np


# считываем данные json файла в переменную data_json
with open('parsing_catalog_imf/json_file/index2.json') as f:
    data_json = json.load(f)

# смотрим что получилось
# print(data_json)

# так как получился словарь, проходим циклом по всем ключам словаря
# for item in data_json:
#     print (item)


# убираем лишние ключи и оставляем нужный (product)
keys = ["partuid", 'total', 'isElastic','slice',"nextslice","partlinks"]
for key in keys:
     data_json.pop(key, None)

# смотрим что получилось
# print(data_json) # получился словарь с одним нужным ключом

# так как получился словарь с значением "список", то проходим циклом по всему списку
# for item in data_json['products']:
#     print (item) # и получаем словари с одинаковыми ключами

# убираем лишние ключи и оставляем нужные

keys_2 = ['uid','sku','text','mark','quantity', 'portion', 'unit', 'single', 'price', 'priceold','descr','gallery','buttonlink','buttontarget',
          "pack_label","pack_x","pack_y","pack_z","pack_m","partuids","externalid",'sort','text','json_options','characteristics']

for item in data_json['products']:
    for key in keys_2:
         item.pop(key, None)

# смотрим что получилось
#print(data_json) # получился словарь с одним нужным ключом

# анализируем ключи...
# print(data_json['products'][0]['editions']) # получился словарь с одним нужным ключом

# for i in data_json['products']:
#     print(i)


# with open('my.json', 'w') as f:
#     json.dump(data_json,f, indent=2)
#
# #for item in data_json['products']:
#     # print (item)
#
# with open('my.json') as f:
#     data = json.load(f)
#
# for item in data['products']:
#     if item['json_options'] !='':
#         item['json_options']=json.loads(item['json_options'])[0]
#         # print (item)
#         # print(type(item['json_options']))
#
# with open('my.json_1', 'w') as f:
#     json.dump(data,f, indent=2)
#
#
#
# for item in data['products']:
#     if item['json_options'] != '':
#         item['json_options'].pop('params', None)
#     #print(item)
#
# with open('my.json_2', 'w') as f:
#     json.dump(data,f, indent=2)
#
#
keys_3 = ['params',"externalid","sku","price","priceold","quantity",'uid']

for item in data_json['products']:
    for i in item['editions']:
        for key in keys_3:
            i.pop(key, None)
        # print(i)


with open('parsing_catalog_imf/json_file/my_14.json', 'w') as f:
    json.dump(data_json['products'],f, indent=2)


with open('parsing_catalog_imf/json_file/my_14.json') as f:
  data = json.load(f)
print(data)

df = pd.json_normalize(data, record_path=['editions'], meta=['title','url'], meta_prefix='products_',
                                    record_prefix='editions_')
df['editions_img'].replace('', np.nan, inplace=True)
df.dropna(subset=['editions_img'], inplace=True)
df['editions_Цвет'] = df['editions_Цвет'].fillna('бесцветный')
for i,e in enumerate (df['editions_Цвет']):
  if '/' in e:
    df['editions_Цвет'][i] = e.replace('/','-')
df['products_title'][221] = df['products_title'][221].replace('/','-')

#print(df)

df.to_csv('parsing_catalog_imf/csv_files/my7_1.csv', index=False)