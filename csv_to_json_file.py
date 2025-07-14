import json
import csv

with (open('playgrounds.csv', encoding='utf-8') as input_file,
      open('addresses.json', 'w', encoding='utf-8') as output_file):
    rows = csv.DictReader(input_file, delimiter=';')
    playgrounds_dict = {}
    for row in rows:
        playgrounds_dict.setdefault(row['AdmArea'], {}).setdefault(row['District'], []).append(row['Address'])
    json.dump(playgrounds_dict, output_file)


'''Вам доступен файл playgrounds.csv с информацией о спортивных площадках Москвы. В первом столбце записан тип площадки,  во втором — административный округ, в третьем — название района, в четвертом — адрес:

ObjectName;AdmArea;District;Address
Парк, озелененная городская территория «Лианозовский парк культуры и отдыха»;Северо-Восточный административный округ;район Лианозово;Угличская улица, дом 13
...
Напишите программу, создающую JSON-объект, ключом в котором является административный округ, а значением — JSON-объект, в котором, в свою очередь, ключом является название района, относящийся к этому административному округу, а значением — список адресов всех площадок в этом районе. Полученный JSON-объект программа должна записать в файл addresses.json.

Примечание 1. Адреса в списках должны располагаться в своем исходном порядке.

Примечание 2. Разделителем в файле playgrounds.csv является точка с запятой, при этом кавычки не используются.'''