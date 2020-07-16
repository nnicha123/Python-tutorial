nums = [1,2,3,4,5,6]

# So we don't have to name the function,
# define and return in same line
print(list(map(lambda n:n*n,nums)))
print(list(map(lambda n:n*n/2,nums)))