import math

# Task I

def normal_cdf(start, end, mean, std):
    cum_dist = lambda obs,mean,std: 0.5*(1+math.erf((obs-mean)/(std*math.sqrt(2))))
    return cum_dist(end, mean, std)-cum_dist(start, mean, std)

print(f'{normal_cdf(0, 9800, 49*205, 15*math.sqrt(49)):.4f}')

# Task II

print(f'{normal_cdf(0, 250, 2.4*100, 2*math.sqrt(100)):.4f}')

# Task III

mean = 500
std = 80
z = 1.96
n = 100

width = z*std/math.sqrt(n)

print(f'{mean+width:.2f}')
print(f'{mean-width:.2f}')
