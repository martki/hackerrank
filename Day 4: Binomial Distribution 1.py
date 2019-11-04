# Enter your code here. Read input from STDIN. Print output to STDOUT

def binomial_cdf(begin, end, total, prob):
    cdf = 0
    for i in range(begin, end+1):
        cdf += binomial_pdf(i, total, prob)
    return cdf

def binomial_pmf(draws, total, prob):
    return combinations(draws, total)*prob**draws*(1-prob)**(total-draws)

def combinations(draws, total):
    return factorial(total)/(factorial(draws)*factorial(total-draws))

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n*factorial(n-1)

print(f'{binomial_cdf(3, 6, 6, 1.09/(1.09+1)):.3f}')
