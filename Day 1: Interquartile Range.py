import math
import fileinput
import itertools


def quartiles(data):
    lower = data[:len(data)//2]
    higher = data[math.ceil(len(data)/2):]

    if len(lower) % 2 != 1:
        first_q = (lower[len(lower)//2-1] + lower[len(lower)//2])/2
    else:
        first_q = lower[math.floor(len(lower)/2)]

    if len(data) % 2 != 1:
        second_q = (data[len(data)//2-1] + data[len(data)//2+1])/2
    else:
        second_q = data[len(data)//2]

    if len(higher) % 2 != 1:
        third_q = (higher[len(higher)//2-1] + higher[len(higher)//2])/2
    else:
        third_q = higher[math.floor(len(lower)/2)]

    return [first_q, second_q, third_q]

for counter, line in enumerate(fileinput.input()):
    if counter == 0:
        continue

    if counter == 1:
        elements = list(map(int, line.split()))
        continue

    frequencies = list(map(int, line.split()))

    data = sorted(list(itertools.chain(*list(map(lambda x,f: [x]*f, elements, frequencies))))) 
    quartiles = quartiles(data)

    print(f'{quartiles[2]-quartiles[0]:.1f}')
