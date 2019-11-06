# Enter your code here. Read input from STDIN. Print output to STDOUT
# Task 1
from math import exp


def poisson_pmf(value, mean):
    return mean**value/fac(value)*exp(-mean)

def fac(num):
    if num == 1 or num == 0:
        return 1
    return num*fac(num-1) 

print(f'{poisson_pmf(5, 2.5):.3f}')


# Task 2

print(f'{160+40*(0.88 + 0.88**2):.3f}')
print(f'{128+40*(1.55 + 1.55**2):.3f}')
