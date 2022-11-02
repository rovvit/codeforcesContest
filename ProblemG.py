# день месяц год
t = int(input())
longMonth = [1, 3, 5, 7, 8, 10, 12]
shortMonth = [4, 6, 9, 11]
a = []
ans = True
isVisok = False
for i in range(t):
    a = input().split(' ')
    a = [int(j) for j in a]
    if a[0] < 1:
        ans = False
    if (a[2] % 4 == 0 and a[2] % 100 != 0) or (a[2] % 400 == 0):
        isVisok = True
    if a[1] in longMonth:
        if a[0] > 31:
                ans = False
    elif a[1] in shortMonth:
        if a[0] > 30:
            ans = False
    else:
        if isVisok:
            if a[0] > 29:
                ans = False
        else:
            if a[0] > 28:
                ans = False
    isVisok = False
    if ans:
        print("YES")
    else:
        print("NO")
    ans = True
