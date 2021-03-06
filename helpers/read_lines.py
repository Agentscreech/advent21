from typing import List

def read_input(day:str) -> List[str]:
    lines = []
    with open(f"{day}/input.txt") as file:
        for line in file:
            lines.append(line)

    return lines


def read_input_comma(day:str) -> List[str]:
    vals = []
    with open(f"{day}/input.txt") as file:
        for line in file:
            vals = line.split(",")

    return vals


def read_input_comma_int(day: str) -> List[int]:
    vals = []
    with open(f"{day}/input.txt") as file:
        for line in file:
            vals = line.split(",")

    for i, value in enumerate(vals):
        vals[i] = int(value)

    return vals

def read_sample_input(day:str) -> List[str]:
    lines = []
    with open(f"{day}/sample_input.txt") as file:
        for line in file:
            lines.append(line)

    return lines