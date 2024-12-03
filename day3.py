import re

with open('day3.txt') as f: s = f.read()

def day3_part1(s):
    # regex pattern to get all mul(x,y)
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    muls = re.findall(pattern, s)
    # regex patter to get x, y
    pattern2 = r"\b\d+\b"
    res = 0

    for m in muls:
        pairs = re.findall(pattern2, m)
        res += int(pairs[0]) * int(pairs[1])
    
    return res

def day3_part2(s):
    # regex pattern to get all mul(x,y) as well as don't() and do()
    pattern = r"mul\(\d{1,3},\d{1,3}\)|do(?:n't)?\(\)"
    expressions = re.findall(pattern, s)
    pattern2 = r"\b\d+\b"
    res = 0
    do = True
    for exp in expressions:
        if exp == "don't()":
            do = False
        elif exp == "do()":
            do = True
        elif do:
            pairs = re.findall(pattern2, exp)
            res += int(pairs[0]) * int(pairs[1])
    return res

print(day3_part1(s))
print(day3_part2(s))