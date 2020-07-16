# ninja_belts = {"crystal":"red","ryu":"black"}
# print(ninja_belts['crystal'])
# print('ryu' in ninja_belts)
# print(list(ninja_belts.keys()))
# vals = list(ninja_belts.values())
# print(vals)
# print(vals.count('red'))
# ninja_belts["yoshi"] = 'red'
# print(ninja_belts)
# vals = list(ninja_belts.values())
# print(vals.count('red'))
# person = dict(name="nicha",age=24,height="164cm")
# print(person)

def ninja_intro(dictionary):
    for key,val in dictionary.items():
        print(f'I am {key} and I am a {val} belt')


ninja_belts = {}

while True:
    ninja_name = input('Enter a ninja name: ')
    ninja_belt = input('Enter a belt color: ')
    ninja_belts[ninja_name] = ninja_belt

    another = input('Add another? (y/n)')
    if another == 'y':
        continue
    else:
        break

ninja_intro(ninja_belts)