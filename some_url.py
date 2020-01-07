"""Имеется набор файлов, каждый из которых, кроме последнего, содержит имя
следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.
"""

import requests

with open(r'C:\Users\oush\Downloads\dataset_3378_3(1).txt') as file:
    url_str = file.readline()
adress = 'https://stepic.org/media/attachments/course67/3.6.3/'
while True:
    url_str = 'http' + url_str[5:len(url_str)]
    print(url_str)
    some_text = requests.get(url_str).text
    print(some_text)
    if 'We' not in some_text:
        url_str = '{}{}'.format(adress, some_text)
    else:
        break
print(some_text)
with open(r'C:\Users\oush\Downloads\reply_3378_4.txt', 'w') as file:
    file.write(some_text)