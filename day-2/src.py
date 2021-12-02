# Day 2

import time 

def main():
    tic = time.perf_counter()
    f = open("input.txt", "r")
    input = [x[:-1] for x in f.readlines()] # eliminates '/n' new line character 
    print(f"Puzzle 1's output is {partOne(input)}")
    print(f"Puzzle 2's output is {partTwo(input)}")
    toc = time.perf_counter()
    print(f"Finished in {toc - tic:0.4f} seconds")

def partOne(input):
    horizontal = 0
    depth = 0 
    for x in input:
        digit = int(''.join(filter(str.isdigit, x))) 
        if 'forward' in x:
            horizontal += digit
        elif 'up' in x:
            depth -= digit
        elif 'down' in x:
            depth += digit
        else:
            print("Error")
            return 0
    return horizontal * depth

def partTwo(input):
    aim = 0
    horizontal = 0
    depth = 0
    for x in input:
        digit = int(''.join(filter(str.isdigit, x)))
        if 'forward' in x:
            horizontal += digit
            depth = depth + aim * digit
        elif 'up' in x:
            aim -= digit
        elif 'down' in x:
            aim += digit
        else:
            print("Error")
            return 0
    return horizontal * depth

if __name__ == "__main__":
    main()