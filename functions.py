# def greet(name='Ryu',time='morning'):
#     print(f'Good {time} {name}, hope you are well')

# # name = input('Enter your name: ')
# # time = input('Enter the time of the day: ')
# greet(name="Nicha")

def area(radius):
    return 3.142*radius*radius
    

def vol(area,length):
    print(area*length)

radius = int(input('Enter a radius: '))
length = int(input('Enter a length: '))

vol(area(radius),length)

