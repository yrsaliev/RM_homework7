## -*- coding: utf-8 -*-

#Make homework a bit trickier. Parse a web site and save data in file

import random
from lxml import html

def get_urls_from_page(url):
    list_of_quantity = []

    path_for_goods = ".//tbody/tr/td[2]/text()"
    path_for_quantity = ".//tbody/tr/td[3]/text()"

    """
    './/' - указывает на то, что для оставшейся части выражения поиск должен производится по всему дереву,

    'span[@class = "productHeadline h3"]' — указывает, что необходимо найти таг 'span' у которого атрибут
        class имеет значение "productHeadline h3" (это та самая отличительная особенность всех тагов которые
        содержат в дочерних элементах), символ '@' - обязательно ставится перед именем атрибута.

    '/a' -  указывает на то что нас интересует не сам таг 'span', а его дочерний таг 'a',

    '/text()' – это XPath функция, которая возвращает текст обрамлённый тагом указанным ранее.

    """

    doc = html.parse(url) #выполняет HTTP GET запрос на скачивание страницы по адресу url, её последующий разбор и
                            # построил соответствующей древовидной иерархии объектов;
                            #  <lxml.etree._ElementTree object at 0x7f38f25518c0>

    goods = doc.xpath(path_for_goods) #в данной строке выполняется поиск всех данных
                                      # удовлетворяющих XPath  выражению. список названий товаров

    quantity = doc.xpath(path_for_quantity) #количество

#На сайте везде стоит значение "кг", здесь в случайном порядке присваиваем значение pieces или pairs
# И запихиваем всё в новый лист

    for element in quantity:
        element = element[:-2]+random.choice(['pieces','pairs'])
        list_of_quantity.append(element)

# соединяем два листа в один словарь. Возвращем словарь как результат работы функции

    final_dict = dict(zip(goods,list_of_quantity))
    return final_dict


#вызов фунции с передачей урла

final_dictionary = get_urls_from_page('http://secondhand.uz.ua/list.html')

#открытие на запись, содержимое файла удаляется, если файла не существует, создается новый.

file = open("price_list", "w")

#запись в файл в формате "название, количество <единица измерения>" и закрытие файла

for key in final_dictionary:
    file.write(key.encode('utf-8')+ ", " +final_dictionary[key].encode('utf-8')+ '\n')

file.close()
