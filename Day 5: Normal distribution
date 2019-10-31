# Enter your code here. Read input from STDIN. Print output to STDOUT
import math


def normal_pdf(obs, mean, std):
    return math.exp(-(obs-mean)**2/(2*std**2))/(std*math.sqrt(2*math.pi))


def normal_cdf(start, end, mean, std):
    cum_dist = lambda obs,mean,std: 0.5*(1+math.erf((obs-mean)/(std*math.sqrt(2))))
    return cum_dist(end, mean, std)-cum_dist(start, mean, std)


# task 1
print(f'{normal_cdf(0, 19.5, 20, 2):.3f}')
print(f'{normal_cdf(20, 22, 20, 2):.3f}')

# task 2
print(f'{normal_cdf(80, 1000, 70, 10)*100:.2f}')
print(f'{normal_cdf(60, 1000, 70, 10)*100:.2f}')
print(f'{normal_cdf(0, 60, 70, 10)*100:.2f}')
