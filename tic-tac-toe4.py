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
newstr = []
newstr.append(test1) 
newstr.append(test2)
newstr.append(test3)
# print(newstr)
# # Vertical
# print(newstr[0][0])
# print(newstr[1][0])
# print(newstr[2][0])

# print(newstr[0][1])
# print(newstr[1][1])
# print(newstr[2][1])

# print(newstr[0][2])
# print(newstr[1][2])
# print(newstr[2][2])

# # Horizontal
# print(newstr[0][0])
# print(newstr[0][1])
# print(newstr[0][2])

# print(newstr[1][0])
# print(newstr[1][1])
# print(newstr[1][2])

# print(newstr[2][0])
# print(newstr[2][1])
# print(newstr[2][2])

# Diagonal
# print(newstr[0][0])
# print(newstr[1][1])
# print(newstr[2][2])

# print(newstr[0][2])
# print(newstr[1][1])
# print(newstr[2][0])
# print(list(test1+test2+test3))