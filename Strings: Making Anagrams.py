#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    
    A = Counter(a)
    B = Counter(b)
    diff = 0
    
    if len(A)>len(B):
        for i in range(len(A)-len(B)):
            B[i] = 0
    if len(B)>len(A):
        for i in range(len(B)-len(A)):
            A[i] = 0

    for a, b in zip(A.keys(), B.keys()):
        if a in B:
            diff += max(A[a], B[a])-min(A[a], B[a])
        if b in A:
            diff += max(B[b], A[b])-min(B[b], A[b])
        if a not in B:
            diff += A[a]
        if b not in A:
            diff += B[b]
        if a in B and a in A:
            diff -= max(A[a], B[a])-min(A[a], B[a])

    return diff

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
