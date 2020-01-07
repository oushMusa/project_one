with open(r'C:\Users\oush\Downloads\dataset_3380_5(1).txt') as file:
    lst_str = file.readlines()
d = {str(i): [] for i in range(1, 12)}
# print(lst_str)
for item in lst_str:
    item = item.split()
    print(item)
    d[item[0]].append(int(item[2]))
print(d)
with open(r'C:\Users\oush\Downloads\reply_3380_5.txt', 'w') as file:
    for i, item in d.items():    
        if len(item) > 0:
            file.write('{} {}\n'.format(i, int(sum(item))/int(len(item))))
            # file.write('\n')
        else:
            file.write('{} -\n'.format(i))