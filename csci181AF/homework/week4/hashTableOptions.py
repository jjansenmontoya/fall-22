import argparse
import heapq
import numpy
import timeit
import random

####################
# Helper Functions
####################


def average(nums):
    """Calculate the sample average."""
    return numpy.average(nums)


def std_dev(nums):
    """Calculate the sample standard deviation."""
    if len(nums) <= 0:
        return numpy.nan

    return numpy.std(nums, ddof=1)


def sec_to_ms(sec):
    """Convert seconds to milliseconds."""
    return sec * 1000.0

def expected_sum(n, k):
    """
    Calculate the sum of sum of the numbers (n-k)..(n-1) inclusive.
    (These will be the "correct" top numbers)
    """
    return n * k - (k * k + k) // 2

def twoChoiceHash(n):
    dict1 = [0]*n
    for i in range(0,n):
        randInt1 = random.randint(0,n-1)
        randInt2 = random.randint(0,n-1)
        if dict1[randInt1] <= dict1[randInt2]:
            dict1[randInt1] += 1
        else:
            dict1[randInt2] += 1
    return max(dict1)

def hashControl(n):
    dict1 = [0]*n
    for i in range(0,n):
        randInt = random.randint(0,n-1)
        dict1[randInt] += 1
    return max(dict1)

def leftChoiceHash(n):
    dictL = [0]*int(n/2)
    dictR = [0]*int(n/2)
    for i in range(0, n):
        randInt1 = random.randint(0,n/2-1)
        randInt2 = random.randint(0,n/2-1)
        if dictR[randInt1] < dictL[randInt2]:
            dictR[randInt1] += 1
        else: 
            dictL[randInt2] += 1
    return max(max(dictL), max(dictR))



if __name__ == "__main__":

    # Command-line parsing
    #   Require user to specify n and k on the command line, and optionally
    #   how many repetitions of the experiment, so we don't have
    #   to edit the file every time we want to make a change.
    parser = argparse.ArgumentParser()
    # The first command-line argument will be called "n".
    # It's an integer.
    parser.add_argument("n", type=int)
    # The second command-line argument will be called "k"
    # It's an  integer.
    # The second command-line argument will be called "experiments"
    # It's an optional integer, and defaults to 1 if not specified
    parser.add_argument("experiments", nargs="?", type=int, default=1)
    args = parser.parse_args()

    control = [0]*args.experiments
    twoChoice = [0]*args.experiments
    leftChoice = [0]*args.experiments

    # Run the experiments
    for i in range(args.experiments):

        # control function
        control[i] = hashControl(args.n)
        # Save the elapsed time
        # Check the answer, and that we haven't changed the original list
        # Display the timing

        # 2-choice hashing
        twoChoice[i] = twoChoiceHash(args.n)
        # Display the timing

        # Left-Hashing
        leftChoice[i] = leftChoiceHash(args.n)
        # Display the timing
    print(f"Average Control\t{average(control)}")
    print(f"Average two choice\t{average(twoChoice)}")
    print(f"Average left choice\t{average(leftChoice)}")
    print(f"Control STD\t{std_dev(control)}")
    print(f"Two Choice STD\t{std_dev(twoChoice)}")
    print(f"Left Choice STD\t{std_dev(leftChoice)}")