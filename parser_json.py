import json
import os

# считываем данные json файла в переменную data_json
with open('parsing_catalog_imf/json_file/index2.json') as f:
    data_json = json.load(f)

# смотрим что получилось
print(data_json)

for item in data_json:
    print (item)



# keys = ["partuid", 'total', 'isElastic','slice',"nextslice","partlinks",'isElastic']
# for key in keys:
#      data_json.pop(key, None)
#
# keys_2 = ['uid','sku','text','mark','quantity', 'portion', 'unit', 'single', 'price', 'priceold','descr','gallery','buttonlink','buttontarget',
#           "pack_label","pack_x","pack_y","pack_z","pack_m","partuids","externalid",'sort']
#
# for item in data_json['products']:
#     for key in keys_2:
#          item.pop(key, None)
#
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
# keys_3 = ['params',"externalid","sku","price","priceold","quantity",'uid']
#
# for item in data['products']:
#     for i in item['editions']:
#         for key in keys_3:
#             i.pop(key, None)
#         print(i)
#
#
# with open('my_4.json', 'w') as f:
#     json.dump(data,f, indent=2)