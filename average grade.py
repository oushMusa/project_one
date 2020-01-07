"""Напишите программу, которая считывает файл с подобной структурой и
для каждого абитуриента выводит его среднюю оценку по этим трём предметам
на отдельной строке, соответствующей этому абитуриенту."""

with open(r'C:\Users\oush\Downloads\dataset_3363_4.txt') as file:
    lst_str = file.readlines()

print(lst_str)
answer = list()

for item in lst_str:
    item = item.split(';')
    item = item[1:len(item)]
    average = sum(map(int, item)) / len(item)    
    answer.append(average)
    
answer_1 = '\n'.join(map(str, answer))
print(answer_1)
arch_item = [0] * len(item)

for item in lst_str:
    item = item.split(';')    
    item = list(map(int, item[1:len(item)]))
    for i, it in enumerate(item):
        arch_item[i] += it

aver_item = [item/len(lst_str) for item in arch_item]
answer_2 = ' '.join(map(str, aver_item))
print(answer_2)

with open(r'C:\Users\oush\Downloads\reply_3363_4.txt', 'w') as file:
    file.write(answer_1)
    file.write('\n')
    file.write(answer_2)    