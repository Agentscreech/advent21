from helpers.read_lines import *
lines = read_input('day05')
"""
Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal, vertical, or a diagonal line at exactly 45 degrees. In other words:

An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
Considering all lines from the above example would now produce the following diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....
You still need to determine the number of points where at least two lines overlap. In the above example, this is still anywhere in the diagram with a 2 or larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?
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
    # lines = read_input('day05')
    parsed = parse_input(sample)
    lines = find_lines(parsed)
    overlaps = count_overlaps(lines)
    print(overlaps)

