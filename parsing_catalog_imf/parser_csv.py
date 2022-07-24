import csv
import os
import requests


with open ('../my7.csv', encoding='utf8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        url = row[0]
        subdir = row[2]
        filename = row[1]
        if not os.path.exists('uploads/'+ subdir):
            os.mkdir('uploads/' + subdir)
        img_data = requests.get(url, verify=True).content
        with open('uploads/' + subdir + '/' + filename , 'wb') as handler:
            handler.write(img_data)
        print(row[2])