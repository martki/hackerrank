#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(s):
    counts = Counter(s)

    v = list(counts.values())[0]
    rem = 0
    for count in counts.values():
        if v == count:
            continue
        else:
            if abs(v-count) > 1 and count != 1:
                return "NO"
            if abs(v-count) == 1 or count == 1:
                rem += 1
                if rem > 1:
                    return "NO"
    
    return "YES"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
