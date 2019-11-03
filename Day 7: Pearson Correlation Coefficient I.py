# Enter your code here. Read input from STDIN. Print output to STDOUT

import fileinput
import math

mean = lambda arr: sum(arr)/len(arr)
std = lambda arr: math.sqrt(sum([(i-mean(arr))**2 for i in arr])/(len(arr)))
cov = lambda X, Y: sum([(X[i]-mean(X))*(Y[i]-mean(Y)) for i in range(len(X))])/len(X)

def pearson(X, Y):
    return cov(X,Y)/(std(X)*std(Y))

for cnt, line in enumerate(fileinput.input()):
    if cnt == 0:
        continue

    if cnt == 1:
        X = list(map(float, line.split()))
    
    if cnt == 2: 
        Y = list(map(float, line.split()))

print(f'{pearson(X,Y):.3f}')
