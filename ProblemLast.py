t = int(input())
for i in range(t):
    flags = [0]*1000000001
    n = int(input())
    blocks = [[0] * 3 for j in range(n)]
    for j in range(n):
        a = input().split(' ')
        for k in range(3):
            blocks[j][k] = int(a[k])
    neighbour = [0 for j in range(n)]
    neighbour[0] = blocks[0][0]
    neighbour[n-1] = blocks[0][2]
    neighbour[1] = blocks[0][1]
    flags[neighbour[0]-1] = 1
    flags[neighbour[1]-1] = 1
    flags[neighbour[n-1]-1] = 1
    for j in range(1, n-1):
        for k in range(n):
            if blocks[k][0] == neighbour[j]:
                if flags[blocks[k][1]-1] == 0:

                    neighbour[j+1] = blocks[k][1]
                    flags[blocks[k][1]-1] = 1
                    break
                else:
                    if flags[blocks[k][2]-1] == 0:
                        neighbour[j+1] = blocks[k][2]
                        flags[blocks[k][2] - 1] = 1
                    break

    for j in range(n//2):
        print(neighbour[j], ' ', neighbour[n//2 + j])
    print()

