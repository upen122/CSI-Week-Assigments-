Task 1 =  http://hackerrank.com/challenges/capitalize/problem?isFullScreen=true

#!/bin/python3
import math
import os
import random
import re
import sys
# Complete the solve function below.
def solve(s):
    return s.title()
            
if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


Task 2 = https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true


def average(array):
    # your code goes here
    distinct_heights = set(arr)
    total = sum(distinct_heights)
    count = len(distinct_heights)
    avg= total / count
    return round(avg , 3)
    
if _name_ == '_main_':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


INPUT = 10
161 182 161 154 176 170 167 171 170 174
OUTPUT = 169.375


Task 3 = https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true

import textwrap

def wrap(string, max_width):
    return '\n'.join(textwrap.wrap(string, max_width))

if _name_ == '_main_':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

INPUT = ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
OUTPUT = ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ


Task 4 https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true

import string

def print_rangoli(size):
    # your code goes here
    alphabets = string.ascii_lowercase
    lines = []

    for i in range(size):
        left = alphabets[size-1:i:-1] 
        middle = alphabets[i:size] 
        row = '-'.join(left + middle)
        lines.append(row.center(4 * size - 3, '-'))

 
    full_rangoli = lines[::-1] + lines[1:]

    for line in full_rangoli:
        print(line)
if _name_ == '_main_':
    n = int(input())
    print_rangoli(n)


INPUT = 5
OUPUT = --------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#NOTE SOLVED WITH THE HELP OF AI 


Task 5 = https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

import string
def merge_the_tools(string, k):
    # your code goes here
    for i in range (0 , len(string), k):
        part = string[i:i+k]
        seen = ''
        for char in part:
            if char not in seen:
                seen += char
        print(seen)
if _name_ == '_main_':
    string, k = input(), int(input())
    merge_the_tools(string, k)

INPUT = AABCAAADA
3
OUPUT = AB
CA
AD
