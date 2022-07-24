import os



path = '../uploads'

print(os.listdir(path))
#
# def obhodFile (path, level=1):
#     print('Level=', level, 'Content:', os.listdir(path))
#     for i in os.listdir(path):
#         if os.path.isdir(path+'/'+i):

#             for i in os.listdir():
#                 per = i + '.jpeg'
#                 os.rename(i, per)
#
#
#     #     print('Спускаемся', path + '/'+i)
#     #     obhodFile(path + '/'+i, level+1)
#     # print('Возвращамеся в', path)

# obhodFile(path)

path = '../uploads'
for item in os.listdir(path):
    for i in os.listdir(path + '/' + item):
        if '.jpeg' not in i:
            per = i + '.jpeg'
            os.rename(path + '/' + item + '/'+i, path + '/' + item + '/'+per)
            print (i)

# path = 'uploads'
# # os.chdir(path)
# for i in os.listdir(path):
#     print(i)
#     per = i+'.jpeg'
#     os.rename(path + '/' + i, path + '/' + per)
