'''Напишите программу, на вход которой подаётся прямоугольная матрица в виде
последовательности строк, заканчивающихся строкой, содержащей только строку
"end" (без кавычек)
Программа должна вывести матрицу того же размера, у которой каждый элемент в
позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j),
(i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной
стороны матрицы.
В случае одной строки/столбца элемент сам себе является соседом по соответствующему
направлению.'''
check = True
matrix = []
str_new = ''
while check == True:
    i = input()
    if i != "end":
        matrix.append(i.split())
    else:
        check = False
# Принимаем массив 
new_matrix = [[0 for i in range(len(matrix[0]))] for n in range(len(matrix))]
# Инициализируем новый массив того же размера
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
# Выполняем условие задания
for item in new_matrix:
    item_str = [str(i) for i in item]    
    item = ' '.join(item_str)
    str_new += item + '\n'
# Приводим в строковый вид
print(str_new)