#Write a Python program to get execution time for a Python method

import timeit
def sum():
    for i in range(1, 10000000):
        i += i
    return i
print(timeit.timeit(lambda: sum(), number=1))