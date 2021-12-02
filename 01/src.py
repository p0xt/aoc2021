# Day 1
import time

def main():
    tic = time.perf_counter()
    f = open("input.txt", "r")
    input = [x[:-1] for x in f.readlines()]
    print(f"Puzzle 1's output is {partOne(input)}")
    print(f"Puzzle 2's output is {partTwo(input)}")
    toc = time.perf_counter()
    print(f"Finished in {toc - tic:0.4f} seconds")

def partOne(input):
    count = 0
    index = 1
    for x in input[1:]:
        if int(x) > int(input[index -1]):
            count = count + 1
        index = index + 1
    return count

def partTwo(input):
    index = 0
    sums = []
    for x in input[:-2]: 
        sums.append(int(input[index]) + int(input[index+1]) + int(input[index+2]))
        index = index + 1
    return partOne(sums)

main()