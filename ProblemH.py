#каждая буква 'a' была закодирована как 00;
#каждая буква 'b' была закодирована как 100;
#каждая буква 'c' была закодирована как 101;
#каждая буква 'd' была закодирована как 11.
t = int(input())
i = 0
while i < t:
    a = input()
    b = [x for x in a]
    j = 0
    while j < len(a):
        if b[j] == '0':
            print('a', end='')
            j +=2
        elif b[j] == '1':
            if b[j+1] == '1':
                print('d', end='')
                j += 2
            elif b[j+2] == '1':
                print('c', end='')
                j += 3
            else:
                print('b', end='')
                j += 3
    print()
    i+=1
