"""
Gary is an avid hiker. He tracks his hikes meticulously, paying close attention to small details like topography. During his last hike he took exactly  steps. For every step he took, he noted if it was an uphill, , or a downhill,  step. Gary's hikes start and end at sea level and each step up or down represents a  unit change in altitude. We define the following terms:

A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
Given Gary's sequence of up and down steps during his last hike, find and print the number of valleys he walked through.

For example, if Gary's path is s=[DDUUUUDD], he first enters a valley  units deep. Then he climbs out an up onto a mountain  units high. Finally, he returns to sea level and ends his hike.

Function Description

Complete the countingValleys function in the editor below. It must return an integer that denotes the number of valleys Gary traversed.

countingValleys has the following parameter(s):

n: the number of steps Gary takes
s: a string describing his path
Input Format

The first line contains an integer , the number of steps in Gary's hike.
The second line contains a single string , of  characters that describe his path.

Constraints
2 <= n <= 10 ^6
s[i] belongs to {UD}

Output Format

Print a single integer that denotes the number of valleys Gary walked through during his hike.

Sample Input

8
UDDDUDUU
Sample Output

1
Explanation

If we represent _ as sea level, a step up as /, and a step down as \, Gary's hike can be drawn as:

_/\      _
   \    /
    \/\/
He enters and leaves one valley.

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    steps_stack = []
    valleys = 0

    for step in s:
        if steps_stack and steps_stack[-1] != step:
            steps_stack.pop()

            if step == 'U' and len(steps_stack) == 0:
                valleys += 1
        else:
            steps_stack.append(step)

    return valleys


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # n = int(input())
    #
    # s = input()
    n = 8
    s = ['D', 'D', 'U', 'U', 'U', 'U', 'D', 'D']
    s = ['U', 'U', 'U', 'U', 'D', 'D', 'D', 'D']
    s = ['D', 'U', 'D', 'U', 'D', 'U', 'D', 'U']
    s = ['U', 'U', 'U', 'D', 'U', 'D', 'D', 'D']
    s = ['U', 'U', 'U', 'U', 'U', 'U', 'U', 'U']
    s = ['D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'U']

    result = countingValleys(n, s)
    print(result)

    # fptr.write(str(result) + '\n')
    #
    # fptr.close()

