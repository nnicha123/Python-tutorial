def f1(x):
    return x**2 + 1

def f2(x):
    return 1/(x**2)

def f3(x):
    return x**2 -1

def f(x):
    if x <= 0:
        result = f1(x)
    elif 0 < x < 1:
        result = f2(x)
    else:
        result = f3(x)
    return result

print(f(1))
print(f(0.1))