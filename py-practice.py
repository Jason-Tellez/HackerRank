##### 1. Python If-Else
#Given an integer, n, perform the following conditional actions:
    #If  is odd, print Weird
    #If  is even and in the inclusive range of 2 to 5, print Not Weird
    #If  is even and in the inclusive range of 6 to 20, print Weird
    #If  is even and greater than 20, print Not Weird
#Input Format:
    #A single line containing a positive integer, n.
#Constraints
    # 1 <= n <= 100
#Output Format:
    #Print Weird if the number is weird. Otherwise, print Not Weird.

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(raw_input().strip())
    if n % 2 == 1:
        print('Weird')
    else:
        if n <= 4:
            print('Not Weird')
        elif n > 4 and n <= 20:
            print('Weird')
        elif n > 20:
            print('Not Weird')



##### 2. Arithmetic Operators
#Task
#The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:
    #1. The first line contains the sum of the two numbers.
    #2. The second line contains the difference of the two numbers (first - second).
    #3. The third line contains the product of the two numbers.

#provided
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(a + b)
    print(a - b)
    print(a * b)



##### 3. Division
#Task
#The provided code stub reads two integers, a and b, from STDIN.
#Add logic to print two lines. The first line should contain the result of integer division,  a//b. 
    #The second line should contain the result of float division, a/b.
#No rounding or formatting is necessary.