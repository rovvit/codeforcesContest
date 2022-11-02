t = int(input())
a = []
for i in range(t):
    clientA = 0
    clientB = 0
    count = 0
    maxCount = -1
    n = int(input())
    a = input().split(' ')
    a = [int(j) for j in a]
    if n == 1:
        print('1')
    elif n == 2:
        print('2')
    else:
        clientA = a[1]
        clientB = a[0]
        count = 2
        for j in range(2, n):
            if a[j] == clientA or a[j] == clientB or clientB == clientA:
                count += 1
                if clientA == clientB:
                    clientA = a[j]
            else:
                if a[j-1] == clientA:
                    clientB = a[j]
                    count = 1
                    for k in range(j-1, 0, -1):
                        if a[j-1] == a[k]:
                            count += 1
                        else:
                            break
                else:
                    clientA = a[j]
                    count = 1
                    for k in range(j-1, 0, -1):
                        if a[j-1] == a[k]:
                            count += 1
                        else:
                            break
            if count > maxCount:
                maxCount = count
        print(maxCount)


