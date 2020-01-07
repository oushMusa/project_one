""" Напишите программу, которая считывает из файла строку, соответствующую тексту,
сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.

Запишите полученный текст в файл и прикрепите его, как ответ на это задание.

Write program, that read a line from a file, which is incripted text.
The text containe chars and nums. Decrypt it.
(Key for decrypting: Duplicate 'char' 'num' times.)
Write your result in new file."""

with open(r'C:\Users\oush\Downloads\dataset_3363_2.txt') as file:
    new_str = file.readline().strip()
lst = [item for item in new_str]
lst_1 = list()
lst_2 = list()
for item in lst:
    if item.isalpha():                 # make a list of chars
        lst_1.append(item)
        lst_2.append('')
    elif item.isalnum:                 # make a list of nums
        lst_2[len(lst_1)-1] += item        
lst = str()
for i, key in enumerate(lst_1):        # make new str
    lst += key * int(lst_2[i])
with open(r'C:\Users\oush\Downloads\reply_3363_2.txt', 'w') as file:
    file.write(lst)