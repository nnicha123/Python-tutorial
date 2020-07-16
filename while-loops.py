age = 25
num = 0

while num < age:
    if num == 0:
        num+=1
        continue
    if num % 2 == 0:
        print(num)
    num+=1
    if num > 10:
        break
    