arr = []
for num in range(1, 1000):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           arr.append(num)
print(arr)