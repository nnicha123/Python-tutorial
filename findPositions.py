
list1 = list(input().split(' '))
list2 = input()
indx = []
index = 0
for el in list1:
    if el == list2:
        indx.append(str(index))
    index +=1
if len(indx) == 0:
    print('not found')
else:
    print(' '.join(indx))