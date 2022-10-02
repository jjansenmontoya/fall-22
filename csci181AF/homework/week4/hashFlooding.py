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
    return n * k - (k * k + k) // 2\

def hashFlooding(n):
    dict = {}
    for i in range(0,n):
        dict[200+(2**61-1)*i] = 0
    return 'Done'

def hashControl(n):
    dict = {}
    for i in range(0,n):
        dict[i] = 0
    return 'Done'


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

    # Run the experiments
    for _ in range(args.experiments):

        # Strategy 1
        t_start = timeit.default_timer()
        hashFlooding(args.n)
        t_stop = timeit.default_timer()
        # Save the elapsed time
        time = t_stop - t_start
        # Check the answer, and that we haven't changed the original list
        # Display the timing
        print(f"HashFlood\t{args.n}\t{sec_to_ms(time)}")

        # Strategy 2
        t_start = timeit.default_timer()
        print(hashControl(args.n))
        t_stop = timeit.default_timer()
        # Save the elapsed time
        time = t_stop - t_start
        # Display the timing
        print(f"HashControl\t{args.n}\t{sec_to_ms(time)}")

        # Strategy 3
        """
        t_start = timeit.default_timer()
        answers = strategy3(numbers, args.k)
        t_stop = timeit.default_timer()
        # Save the elapsed time
        time = t_stop - t_start
        # Check the answer, and that we haven't changed the original list
        assert sum(answers) == expected_sum(args.n, args.k)
        assert sum(numbers) == args.n * (args.n - 1) // 2
        # Display the timing
        print(f"3\t{args.n}\t{args.k}\t{sec_to_ms(time)}")
        """

        # Strategy 4
        """
        t_start = timeit.default_timer()
        answers = strategy4(numbers, args.k)
        t_stop = timeit.default_timer()
        # Save the elapsed time
        time = t_stop - t_start
        # Check the answer, and that we haven't changed the original list
        assert sum(answers) == expected_sum(args.n, args.k)
        assert sum(numbers) == args.n * (args.n - 1) // 2
        # Display the timing
        print(f"4\t{args.n}\t{args.k}\t{sec_to_ms(time)}")
        """

        # Strategy 5
        """
        t_start = timeit.default_timer()
        answers = strategy5(numbers, args.k)
        t_stop = timeit.default_timer()
        # Save the elapsed time
        time = t_stop - t_start
        # Check the answer, and that we haven't changed the original list
        assert sum(answers) == expected_sum(args.n, args.k)
        assert sum(numbers) == args.n * (args.n - 1) // 2
        # Display the timing
        print(f"5\t{args.n}\t{args.k}\t{sec_to_ms(time)}")
        """