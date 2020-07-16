from random import shuffle

def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram)


words = ['beetroot','carrots','potatoes']
anagrams = []

# Method 1)
# for word in words:
#     anagrams.append(jumble(word))
# print(anagrams)

# Method 2)
# print(list(map(jumble,words)))

# Method 3)
print([jumble(word) for word in words])
