# Enter your code here. Read input from STDIN. Print output to STDOUT

input()
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

def spearman_corr(X, Y):
    X_r = [sorted(X).index(x) for x in X]
    Y_r = [sorted(Y).index(y) for y in Y]
    D = [(x-y)**2 for x, y in list(zip(X_r, Y_r))]
    
    return 1 - (6 * sum(D))/(len(X)*(len(X)**2-1))

print(f'{spearman_corr(X, Y):.3f}')
