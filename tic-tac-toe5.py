import math
import re
print('Enter cells:')
in1 = input()
in2 = list(in1)
test1 = in2[0:3]
test2 = in2[3:6]
test3 = in2[6:9]
str1 = '| ' + ' '.join(test1) + ' |'
str2 = '| ' + ' '.join(test2) + ' |'
str3 = '| ' + ' '.join(test3) + ' |'

totalStr = '---------\n' + str1 + '\n' + str2 + '\n' + str3 + '\n' + '---------'
print(totalStr)

while(True):
    print('Enter the coordinates:')
    coord = input().split(' ')
    if(not bool(re.match("\d",coord[0])) or not bool(re.match("\d",coord[1]))):
        print('You should enter numbers!')
    elif(int(coord[0]) > 3 or int(coord[1]) > 3 or int(coord[0]) < 0 or int(coord[1]) < 0):
        print('Coordinates should be from 1 to 3!')
    elif coord[0] == '1' and coord[1] == '3':
        if(test1[0] == '_'):
            test1[0] = 'X'
            break
        else:
            print('This cell is occupied! Choose another one!')

    elif coord[0] == '2' and coord[1] == '3':
        if(test1[1] == '_'):
            test1[1] = 'X'
            break
        else:
            print('This cell is occupied! Choose another one!')
    elif coord[0] == '3' and coord[1] == '3':
        if(test1[2] == '_'):
            test1[2] = 'X'
            break
        else:
            print('This cell is occupied! Choose another one!')

    elif coord[0] == '1' and coord[1] == '2':
        if(test2[0] == '_'):
            test2[0] = 'X'
            break
        else:
            print('This cell is occupied! Choose another one!')
    elif coord[0] == '2' and coord[1] == '2':
        if(test2[1] == '_'):
            test2[1] = 'X'
            break
        else:
            print('This cell is occupied! Choose another one!')
    elif coord[0] == '3' and coord[1] == '2':
        if(test2[2] == '_'):
            test2[2] = 'X'
            break
        else:
            print('This cell is occupied! Choose another one!')

    elif coord[0] == '1' and coord[1] == '1':
        if(test3[0] == '_'):
            test3[0] = 'X'
            break
        else:
            print('This cell is occupied! Choose another one!')
    elif coord[0] == '2' and coord[1] == '1':
        if(test3[1] == '_'):
            test3[1] = 'X'
            break
        else:
            print('This cell is occupied! Choose another one!')
    elif coord[0] == '3' and coord[1] == '1':
        if(test3[2] == '_'):
            test3[2] = 'X'
            break
        else:
            print('This cell is occupied! Choose another one!')
    
str1 = '| ' + ' '.join(test1) + ' |'
str2 = '| ' + ' '.join(test2) + ' |'
str3 = '| ' + ' '.join(test3) + ' |'

totalStr = '---------\n' + str1 + '\n' + str2 + '\n' + str3 + '\n' + '---------'
print(totalStr)