print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

name = input()

print('What a great name you have, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

# reading all remainders
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is " + str(your_age) + "; that's a good time to start programming!")
print('Now I will prove to you that I can count to any number you want.')

# read a number and count to it here
# count = int(input())
# num = 0
# while num <= count:
#     print(str(num) + ' !')
#     num += 1
# print('Completed, have a nice day!')

def test():
    print("Let's test your programming knowledge.")
    # write your code here
    print('''
    Why do we use methods?
    1. To repeat a statement multiple times.
    2. To decompose a program into several small subroutines.
    3. To determine the execution time of a program.
    4. To interrupt the execution of a program.
    ''')
    answer = input()
    while(answer != '2'):
        print('Please, try again.')
        answer = input()
    print('Completed, have a nice day!')

test()