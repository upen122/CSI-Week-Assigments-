# Task 1
# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a+b)
print(a-b)
print(a*b)

INPUT = 3 , 2 , OUPUT = 5 , 1 , 6  


# Task 2
# In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .
# You are given a string . Suppose a character '' occurs consecutively  times in the string. Replace these consecutive occurrences of the character '' with  in the string.

from itertools import groupby

# Read input
s = input()

# Apply groupby and print results
result = [(len(list(g)), int(k)) for k, g in groupby(s)]
print(' '.join(str(item) for item in result))

INPUT = 1222311 , OUTPUT = (1, 1) (3, 2) (1, 3) (2, 1)


# Task 3
# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

# Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.


def is_leap(year):
    leap = False

    # Correct logic here
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            leap = True

    return leap

year = int(input())
print(is_leap(year))

INPUT = 1990 , OUTPUT = False

# Task 4

# The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.

# To read more about the functions in this module, check out their documentation here.

# You are given a list of  lowercase English letters. For a given integer , you can select any  indices (assume -based indexing) with a uniform probability from the list.

# Find the probability that at least one of the  indices selected will contain the letter: ''.

from itertools import combinations
n = int(input())
letters = input().split()
k = int(input())

all_combinations = list(combinations(letters, k))
favorable = [comb for comb in all_combinations if 'a' in comb]

probability = len(favorable) / len(all_combinations)
print(f"{probability:.3f}")

INPUT = 4
a a c d
2 
OUTPUT = 0.833

# Task 5

# Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .

# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

n = int(input())
ele = (map(int , input().split()))
tup = tuple(ele)
print(hash(tup))

INPUT = 3
14
OUTPUT = -3644245484948896500

# NOTE OUTPUT IS COMING IN NEGETIVE WHICH IS NORMAL IN HASH FUNCTION NOTHING TO FIX THIS 


#Task 6 

# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

# Read the dictionary containing student names and their marks
n = int(input())
students = {}

for _ in range(n):
    data = input().split()
    name = data[0]  
    marks = list(map(float, data[1:])) 
    students[name] = marks 
query_name = input()
if query_name in students:
    avg_marks = sum(students[query_name]) / len(students[query_name])
    print(f"{avg_marks:.2f}")
else:
    print("Student not found.")

INPUT = 3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

OUPUT = 56.00


# NOTE = THE CODE WAS ALREADY GIVING WE HAVE TO FIND OUT THE ERROR !!!


# Task 7

# Given an integer, , print the following values for each integer  from  to :

# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary
# Function Description

# Complete the print_formatted function in the editor below.

# print_formatted has the following parameters:

# int number: the maximum value to print


def print_formatted(number):
      width = len(bin(number)[2:])
      for i in range(1, number + 1):
        dec = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexa = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)
        print(f"{dec} {octal} {hexa} {binary}")
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

INPUT = 2 , OUTPUT =  1  1  1  1
                      2  2  2 10



# Task 8

# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules

# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string .


def minion_game(string):
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    length = len(string)

    for i in range(length):
        if string[i].upper() in vowels:
            kevin_score += length - i
        else:
            stuart_score += length - i

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

INPUT = BANANA , OUTPUT = Stuart 12 

# NOTE = USING CHATGPT FOR THE IDEA AND UNDERSTANDING IN THIS TASK !! 


