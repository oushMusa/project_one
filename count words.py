"""Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки)
и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось.
Если таких слов несколько, вывести лексикографически первое """

with open(r'C:\Users\oush\Downloads\Библия.txt') as file:
    lst_str = file.readlines()
d_str = {}
list_d = []
for item in lst_str:
    item = item.split()
    max_var = 1
    d_str = {word:item.count(word) for word in set(item) \
               if word not in d_str.keys() or item.count(word) > d_str[word]}
    list_d.append(d_str)    
print(list_d)
d_str = {'':0}
for item in list_d:
    new = max(item.values())
    new_1 = {i: new for i in item.keys() if item[i] == new}    
    if max(new_1.values()) > max(d_str.values()):
        d_str = new_1.copy()
new = list(sorted(d_str.items()))
new = ' '.join(map(str, new[0]))
print(new)
with open(r'C:\Users\oush\Downloads\reply_3363_3.txt', 'w') as file:
    file.write(new)