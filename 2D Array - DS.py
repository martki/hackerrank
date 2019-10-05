#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    highest_sum = -sys.maxsize

    hourglass = [(0,0), (0,1), (0,2), (1,1), (2,0), (2,1), (2,2)]

    x_value = 0 
    y_value = 0
    hourglass_sum = 0

    for _ in range((len(arr))*len(arr[0])):

        hourglass_sum = 0

        try:
            for (x, y) in hourglass:
                hourglass_sum += arr[x_value+x][y_value+y]

            if highest_sum < hourglass_sum:
                highest_sum = hourglass_sum 
            y_value += 1
            
        except IndexError:
            x_value += 1
            y_value = 0
 
    return highest_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
