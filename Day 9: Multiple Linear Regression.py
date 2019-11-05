# Enter your code here. Read input from STDIN. Print output to STDOUT
from sklearn import linear_model
import numpy as np


X = []
Y = []
pred = []

a, b = map(int, input().split())
for _ in range(b):
    v = list(map(float, input().split()))
    X.append(v[:-1])
    Y.append(v[-1])

c = int(input())
for _ in range(c):
    pred.append(list(map(float, input().split())))

lm = linear_model.LinearRegression()
lm.fit(X, Y)
a = lm.intercept_
b = lm.coef_

for y in pred:
    print(float(lm.predict(np.array(y).reshape(1, -1))))
