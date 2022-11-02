t = int(input())
a = []
b = [0]*1000
max = -1
for i in range(t):
    n = int(input())
    a = (input())
    a = a.replace(':', ' ').replace('H', ' ').split(' ')
    a = [int(j) for j in a]

    for j in range(n):
        b[a[j]] += 1
        if a[j] > max:
            max = a[j]
    for j in range(1, max+1):
        for k in range(b[j]):
            print(j, end=" ")
        b[j] = 0
    max = -1
    print()


# b[a[i]]++
# for (i = 0; i < max; i++)
# for (j = 0; j < b[i], j++) sout (i)

# 6         t
# 1         n
# 1         a[]
# 2
# 1 2
# 3
# 1 2 3
# 4
# 1 2 3 4
# 5
# 1 2 3 4 5
# 6
# 1 2 3 4 5 6

