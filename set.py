empty_set = set()
print(type(empty_set))   # <class 'set'>
 
empty_dict = {}
print(type(empty_dict))  # <class 'dict'>
flowers = {'rose', 'lilac', 'daisy'}
 
# the order is not preserved
print(flowers)  # {'daisy', 'lilac', 'rose'}  

letters = set('philharmonic')
print(letters)  # {'h', 'r', 'i', 'c', 'o', 'l', 'a', 'p', 'm', 'n'}

letters = set('Hello')
print(len(letters))  # the length equals 4
print(letters)       # {'H', 'e', 'o', 'l'}