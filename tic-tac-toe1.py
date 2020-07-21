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