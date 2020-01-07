input_num = int(input())               
matrix = [[0 for i in range(input_num)] for i in range(input_num)] # initialize the matrix
step = 1
i, j = 0, 0  # coordinates of beginning of line
direction = 1 # direction of drowing
start_1, finish_1 = 0, input_num       # borders of function (top of the square)
start_2, finish_2 = 1, input_num       # borders of function (right side of the square)
start_3, finish_3 = input_num - 2, -1  # borders of function (bottom of the square)
start_4, finish_4 = input_num - 2, 0   # borders of function (left side of the square)
while step <= input_num**2:
    if direction == 1:                 # draw the top of the square
        for j in range(start_1, finish_1):
            matrix[i][j] = step
            step += 1
        direction = 2
        start_1 += 1
        finish_1 -= 1
    elif direction == 2:               # draw the right side of the square
        for i in range(start_2, finish_2):
            matrix[i][j] = step
            step += 1
        direction = 3
        start_2 += 1
        finish_2 -= 1
    elif direction == 3:               # draw the bottom of the square
        for j in range(start_3, finish_3, -1):
            matrix[i][j] = step
            step += 1
        direction = 4
        start_3 -= 1
        finish_3 += 1
    else:                             # draw the left side of the square
        for i in range(start_4, finish_4, -1):
            matrix[i][j] = step
            step += 1
        direction = 1
        start_4 -= 1
        finish_4 += 1        
for i in range(input_num):                      # make strings
    print(' '.join(map(str, matrix[i])))