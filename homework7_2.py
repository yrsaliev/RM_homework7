## -*- coding: utf-8 -*-

"""
Выполнить первое задание считав все значения из csv
"""

import csv

reader = csv.reader(open("price_list (copy)","rb"))
pairs=0
pieces=0

for row in reader:
    try:
        if 'pieces' in row[1]:
            pieces +=1
        elif 'pairs' in row[1]:
            pairs+=1
    except:
        break

writer = csv.writer(open("price_list (copy)","a"))

writer.writerows([
    ['Количество товаров которые считаются штуками:', str(pieces)],
    ['Количество товаров, которые считаются парами:', str(pairs)]
    ])
