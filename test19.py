import random


# # this line is needed for us to check the results, don't modify it please
# random.seed(int(input()))

# # use a function from the random module in the next line
# print(random.randint(1,6))

import random


random.seed(3)
# call the function here
print(random.betavariate(alpha=0.9, beta=0.1))