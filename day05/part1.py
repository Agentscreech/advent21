from helpers.read_lines import *


"""
They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.
For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

So, the horizontal and vertical lines from the above list would produce the following diagram:

.......1..
..1....1..
..1....1..
.......1..
.112111211
..........
..........
..........
..........
222111....
In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

Consider only horizontal and vertical lines. At how many points do at least two lines overlap?
"""

sample = read_sample_input('day05')

def parse_input(lines):
    output = []
    for line in lines:
        first, second = line.split(' -> ')
        x1, y1 = first.split(',')
        x2, y2 = second.split(',')
        output.append((int(x1), int(y1), int(x2), int(y2)))
    return output

def find_lines(lines):
    output = []
    for line in lines:
        x1, y1, x2, y2 = line
        if x1 == x2:
            output.append((x1, y1, x2, y2))
        elif y1 == y2:
            output.append((x1, y1, x2, y2))
    return output

def count_overlaps(lines: list) -> int:
    output = {}
    for line in lines:
        x1, y1, x2, y2 = line
        if x1 == x2:
            spaces = abs(y2 - y1)
            if y1 > y2:
                for i in range(spaces+1):
                    if (x2, y2+i) not in output:
                        output[(x2, y2+i)] = 1
                    else:
                        output[(x2, y2+i)] += 1
            else:
                for i in range(spaces+1):
                    if (x1, y1+i) not in output:
                        output[(x1, y1+i)] = 1
                    else:
                        output[(x1, y1+i)] += 1
        elif y1 == y2:
            spaces = abs(x1 - x2)
            if x1 > x2:
                for i in range(spaces+1):
                    if (x2+i, y2) not in output:
                        output[(x2+i, y2)] = 1
                    else:
                        output[(x2+i, y2)] += 1
            else:
                for i in range(spaces+1):
                    if (x1+i, y1) not in output:
                        output[(x1+i, y1)] = 1
                    else:
                        output[(x1+i, y1)] += 1
    sum = 0
    for key in output:
        if output[key] >= 2:
            sum += 1
    return sum

def run():
    lines = read_input('day05')
    parsed = parse_input(lines)
    lines = find_lines(parsed)
    overlaps = count_overlaps(lines)
    print(overlaps)