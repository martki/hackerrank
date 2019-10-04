# Enter your code here. Read input from STDIN. Print output to STDOUT

import fileinput
import numpy as np
from scipy import stats


for counter, line in enumerate(fileinput.input()):
    if counter == 0:
        continue
    number_array = list(map(int, line.split(" ")))

    print(f'{np.mean(number_array):.1f}')
    print(f'{np.median(number_array):.1f}')
    print(f'{stats.mode(number_array)[0][0]}')
