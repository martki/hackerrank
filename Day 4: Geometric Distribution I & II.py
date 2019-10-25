def geometric_pmf(success, total, prob):
    return prob**success*(1-prob)**(total-success)

def geometric_cdf(success, total, prob):
    return sum([geometric_pmf(success, i, prob) for i in range(1, total+1)])

print(f'{geometric_pmf(1, 5, 1/3):.3f}')
print(f'{geometric_cdf(1, 5, 1/3):.3f}')


