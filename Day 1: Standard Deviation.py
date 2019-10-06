import fileinput
import math


mean = lambda data: sum(data)/len(data)
std = lambda data, mean: math.sqrt((sum([(x-mean)**2 for x in data])/len(data)))

for counter, line in enumerate(fileinput.input()):
    if counter == 0:
        continue

    data = list(map(int, line.split()))
    mean = mean(data)

    print(f'{std(data, mean):.1f}')