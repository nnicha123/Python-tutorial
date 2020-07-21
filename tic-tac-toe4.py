import math
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

newstr = []
newstr.append(test1) 
newstr.append(test2)
newstr.append(test3)

# Check win
horizonX = 0
horizonO = 0
Xwin = 0
Owin = 0
countX = 0
countO = 0
for i in range(0,3):
    horizonX = 0
    horizonO = 0
    for j in range(0,3):
        if newstr[i][j] == 'X':
            horizonX += 1
            countX += 1
            if horizonX == 3:
                Xwin = 1
        elif newstr[i][j] == 'O':
            horizonO += 1
            countO += 1
            if horizonO == 3:
                Owin = 1
# Vertical win
verX = 0
verO = 0
for i in range(0,3):
    verX = 0
    verO = 0
    for j in range(0,3):
        if newstr[j][i] == 'X':
            verX += 1
            if verX == 3:
                Xwin += 1
        elif newstr[j][i] == 'O':
            verO += 1
            if verO == 3:
                Owin += 1

if (newstr[0][0] == 'X' and newstr[1][1] == 'X' and newstr[2][2] == 'X') or (newstr[0][2] == 'X' and newstr[1][1] == 'X' and newstr[2][0] == 'X'):
    Xwin += 1
elif (newstr[0][0] == 'O' and newstr[1][1] == 'O' and newstr[2][2] == 'O') or (newstr[0][2] == 'O' and newstr[1][1] == 'O' and newstr[2][0] == 'O'):
    Owin += 1

print(totalStr)
if (Xwin == 1 and Owin == 1) or math.fabs(countX - countO) >=2:
    print('Impossible')
elif Xwin == 1:
    print('X wins')
elif Owin == 1:
    print('O wins')
elif countX + countO < 9:
    print('Game not finished')
elif Xwin == Owin:
    print('Draw')