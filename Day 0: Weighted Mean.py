import fileinput

weighted_mean = lambda values, weights: sum([v*w for (v, w) in zip(values, weights)])/sum(weights)

for counter, line in enumerate(fileinput.input()):
    if counter == 0:
        continue
    
    if counter == 1:
        values = list(map(int, line.split(" ")))
    
    if counter == 2:
        weights = list(map(int, line.split(" ")))
    
        w_mean = weighted_mean(values, weights)
        print(f'{w_mean:.1f}')
