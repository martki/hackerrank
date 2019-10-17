#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribes = 0
    
    for i, v in enumerate(q, start=1):
        
        if v > i + 2:
            print("Too chaotic")
            return
        
        if v <= i:
            for j in range(i-1):
                if q[j] > v:
                    bribes += 1

    print(bribes)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
