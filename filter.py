grades = ['A','B','F','C','F','A']

def remove_fails(grade):
    return grade != 'F'

print(list(filter(remove_fails,grades)))

print([grade for grade in grades if grade!='F'])