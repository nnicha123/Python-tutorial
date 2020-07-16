def cough_dec(func):
    def func_wrapper():
        print('*cough*')
        # Code before function
        func()
        print('*cough*')
    return func_wrapper

@cough_dec
def question():
    print('Can you give me a discount on that?')

@cough_dec
def answer():
    print('it\'s only 50p')

question()
answer()