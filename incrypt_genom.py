sample_str = 'aaaabbcaa'
sample_list = list(sample_str)
my_char = sample_str[0]
i = 0
new_list = list()
for ind, symbol in enumerate(sample_list):
    if my_char == symbol:
        i += 1
    else:
        new_list.append('{}{}'.format(sample_list[ind-1], str(i)))
        i = 1
        my_char = symbol
        print(new_list) 
new_list.append('{}{}'.format(symbol, str(i)))
sample_str = ''.join(new_list)
print(sample_str)