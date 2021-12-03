import time

def main():
    tic = time.perf_counter()
    f = open("input.txt", "r")
    input = [x[:-1] for x in f.readlines()]
    print(input)
    print(f"Puzzle 1's output is {partOne(input)}")
    print(f"Puzzle 2's output is {partTwo(input)}")
    toc = time.perf_counter()
    print(f"Finished in {toc - tic:0.4f} seconds")

# Part one
def getGamma(input):
    gamma = []
    for x in input:
        ones = 0         # count how many 1s
        zeros = 0        # count how many 0s
        for i in x:
            print(f"i is {i}")
            if i == "1":
                ones += 1
            elif i == "0":
                zeros += 1
            else:
                print("Error while checking if item is 1 or 0")
        if ones > zeros:
            gamma.append(1)
        elif ones < zeros:
            gamma.append(0)
        else:
            print("Error while checking the most common item")
    print(f"gamma is {gamma}")
    return int(gamma)

def partOne(input):
    getGamma(input)


# Part two
def partTwo(input):
    return 0



if __name__ == "__main__":
    main()