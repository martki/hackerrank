import fileinput
import math

# not allowed to use other packages than math
for counter, line in enumerate(fileinput.input()):
    if counter == 0:
        continue

    data = sorted(list(map(int, line.split(" "))))
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
        
    print(f'{int(first_q)}\n{int(second_q)}\n{int(third_q)}')

