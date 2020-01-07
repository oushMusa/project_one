rows, colums, mines = [int(i) for i in input().split()]
mine_coordinates = [tuple([int(i) for i in input().split()]) for i in range(mines)]
fild = [[0 for i in range(colums)] for i in range(rows)]
for i, j in mine_coordinates:
    fild[i][j] = '*'
    print(i, j)
print(mine_coordinates)
print(fild)
