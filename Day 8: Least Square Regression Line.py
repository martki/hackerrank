# Enter your code here. Read input from STDIN. Print output to STDOUT
import fileinput
import math


X = []
Y = []
for line in fileinput.input():
    s_line = line.split()
    X.append(int(s_line[0]))
    Y.append(int(s_line[1]))

mean = lambda arr: sum(arr)/len(arr)
std = lambda arr: math.sqrt(sum([(i-mean(arr))**2 for i in arr])/(len(arr)))
cov = lambda X, Y: sum([(X[i]-mean(X))*(Y[i]-mean(Y)) for i in range(len(X))])/len(X)

def pearson(X, Y):
    return cov(X,Y)/(std(X)*std(Y))

def b(X, Y):
    return pearson(X, Y) * (std(Y)/std(X))

def a(X, Y):
    return mean(Y) - b(X,Y)*mean(X)

def pred(x_p, X, Y):
    return a(X, Y) + b(X, Y)*x_p
    
print(pred(80, X, Y))
