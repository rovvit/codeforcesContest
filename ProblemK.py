t = int(input())

for i in range(t):
    a = input().split(' ')
    a = [int(j) for j in a]
    coordinates = ['']*a[0]
    count = [[0]*a[1] for i in range(a[0])]
    for x in range(a[0]):
        coordinates[x] = input()
        coordinates[x] = [*coordinates[x]]
    for x in range(a[0]):
        for y in range(a[1]):
            if coordinates[x][y] == '*':
                if x > 0:
                    if coordinates[x-1][y] == '*':
                        count[x][y] = count[x][y]+ 1
                if y > 0:
                    if coordinates[x][y-1] == '*':
                        count[x][y] = count[x][y] + 1
                if x < a[0]-1:
                    if coordinates[x+1][y] == '*':
                        count[x][y] = count[x][y]+ 1
                if y < a[1]-1:
                    if coordinates[x][y+1] == '*':
                        count[x][y] = count[x][y]+ 1
                if count[x][y] % 2 == 1:
                    xstart = x
                    ystart = y
    x = xstart
    y = ystart
    move = True
    while move:
        move = False
        if x > 0:
            if coordinates[x - 1][y] == '*':
                count[x][y] = count[x][y] - 1
                coordinates[x][y] = '.'
                x = x - 1
                print('U', end='')
                move = True

        if y > 0:
            if coordinates[x][y - 1] == '*':
                count[x][y] = count[x][y] - 1
                coordinates[x][y] = '.'
                y = y - 1
                print('L', end='')
                move = True
        if x < a[0] - 1:
            if coordinates[x + 1][y] == '*':
                count[x][y] = count[x][y] - 1
                coordinates[x][y] = '.'
                x = x + 1
                print('D', end='')
                move = True
        if y < a[1] - 1:
            if coordinates[x][y + 1] == '*':
                count[x][y] = count[x][y] - 1
                coordinates[x][y] = '.'
                y = y + 1
                print('R', end='')
                move = True
    print()









