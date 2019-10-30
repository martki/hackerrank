#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.

def swap_sort(arr):
    swaps = 0

    while sorted(arr) != arr:
        for cnt, elem in enumerate(arr, start=1):
            if cnt != elem:
                temp = arr[cnt-1]
                temp2 = arr[elem-1]

                arr[cnt-1] = temp2
                arr[elem-1] = temp

                swaps += 1    
                print(swaps)

    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = swap_sort(arr)

    fptr.write(str(res) + '\n')

    fptr.close()