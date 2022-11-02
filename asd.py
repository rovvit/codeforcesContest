t = int(input())
data = {}

for i in range(t):
  n = int(input())
  curr_list = []
  for j in range(n):
    elements = [int(i )for i in input().split(' ')]
    curr_list.append(elements)
    data.update({n:curr_list})
for number, items in data.items():
    mylist = []
    for count in range(number):
        if count == 0:
            mylist.extend([items[count][1], items[count][0], items[count][2]])
        else:
            if items[count][0] in mylist:
                if items[count][1] in mylist:
                    if items[count][2] in mylist:
                        if len(mylist) == number:
                            break
                        else:
                            continue
                    else:
                        mylist.insert(0, items[count][2])
                else:
                    mylist.insert(0, items[count][1])

            else:
                if items[count][1] in mylist:
                    if items[count][0] not in mylist:
                        mylist.insert(0, items[count][0])
                    if items[count][2] not in mylist:
                        mylist.insert(0, items[count][2])
                else:
                    mylist.insert(0, items[count][0])

    for j in range(n//2):
        print(mylist[j], ' ', mylist[j+n//2])
    print()