#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    m = Counter(magazine)
    #print("m",m)
    n = dict(Counter(note))
    #print("n",n)
    for k, v in Counter(note).items():
       if m[k] < v: 
            return False
    return True

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    result = checkMagazine(magazine, note)
    if result:
        print("Yes")
    else:
        print("No")
