check = True
matrix = []
str_new = ''
while check == True:
    i = input()
    if i != "end":
        matrix.append(i.split())
    else:
        check = False
#colums = len(matrix[0])
#rows = len(matrix)
new_matrix = [[0 for i in range(len(matrix[0]))] for n in range(len(matrix))]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if i < len(matrix)-1 and j < len(matrix[0])-1:
            new_matrix[i][j] = int(matrix[i-1][j]) + int(matrix[i+1][j]) + int(matrix[i][j-1]) + int(matrix[i][j+1])
        elif i == len(matrix)-1 and j != len(matrix[0])-1:
            new_matrix[i][j] = int(matrix[i-1][j]) + int(matrix[0][j]) + int(matrix[i][j-1]) + int(matrix[i][j+1])
        elif j == len(matrix[0])-1 and i != len(matrix)-1:
            new_matrix[i][j] = int(matrix[i-1][j]) + int(matrix[i+1][j]) + int(matrix[i][j-1]) + int(matrix[i][0])
        else:
            new_matrix[i][j] = int(matrix[i-1][j]) + int(matrix[0][j]) + int(matrix[i][j-1]) + int(matrix[i][0])
for item in new_matrix:
    item_str = [str(i) for i in item]    
    item = ' '.join(item_str)
    str_new += item + '\n'
print(str_new)
print(new_matrix)