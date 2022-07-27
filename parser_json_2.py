import json
import os


url = 'https://store.tildacdn.com/api/getproductslist/?storepartuid=105150852661&recid=420874855&c=1658871063166&getparts=true&getoptions=true&slice=1&&size=100'

with open('parsing_catalog_imf/json_file/filename.json') as f:
    data_json_2 = json.load(f)


for item in data_json_2:
    item.pop('products_json_options')
    item.pop('products_characteristics')
    print(item)


with open('my_5.json', 'w') as f:
   json.dump(data_json_2,f, indent=2)

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