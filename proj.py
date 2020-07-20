import random
wordList = ['python', 'java', 'kotlin', 'javascript']
indx = random.randint(0,len(wordList)-1)

print('''
H A N G M A N
Guess the word:
''')
word = input()
if(word == wordList[indx]):
    print('You survived!')
else:
    print('You are hanged!')