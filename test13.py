empty_tuple = ()
print(type(empty_tuple))

now_a_tuple = ('cat',)
print(now_a_tuple)        # ('cat',)
print(type(now_a_tuple))  # <class 'tuple'>

weekend = 'Saturday', 'Sunday'
print(weekend)        # ('Saturday', 'Sunday')
print(type(weekend))  # <class 'tuple'>

# a tuple from a string
sound = tuple('meow')
print(sound)  # ('m', 'e', 'o', 'w')