# # put your python code here
# import math
# a = int(input())
# b = int(input())
# c = int(input())
# p = (a+b+c)/2
# S = math.sqrt(p*(p-a)*(p-b)*(p-c))
# print(S)

import math
# angle = int(input())
# radians = angle* math.pi/180
# print(round(1/math.tan(radians),10))

in1 = int(input())
in2 = int(input())
if(in2 > 1):
    print(round(math.log(in1,in2),2))
else:
    print(round(math.log(in1),2))


