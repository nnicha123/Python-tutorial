# print('ladies'.endswith('s'))
words = list(input().split(' '))
newword = []
for word in words:
    if(word.endswith('s')):
        newword.append(word)
print('_'.join(newword))