#! /usr/bin/env python3

import argparse
import random


def throwDart():
    """
    Throw a dart and return whether it hits the circle.
    Dart is placed randomly in a 2x2 square, where
       x and y are between -1 and 1.
    The circle is a unit circle centered at the origin.
    The square has area 4, the circle has area π*1*1= π,
    so there probability of hitting the circle is π/4.
    """
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    return x * x + y * y <= 1


def approximate(n):
    """
    Approximate π by throwing n darts.
    We throw n darts, and count how many hit.
    The fraction of darts that hit should be π/4.
    So 4 times that fraction should be π.
    """
    hits = 0
    throws = 0
    for _ in range(n):
        throws += 1
        hits += int(throwDart())

    pi = 4 * hits / throws
    return pi


if __name__ == "__main__":

    # Command-line parsing
    #   Allow user to specify on the command line how many darts
    #   and how many repetitions of the experiment, so we don't have
    #   to edit the file every time we want to make a change.
    # E.g.,
    #   python pi.py
    #         to throw the default of 1000 darts and report the estimate.
    #   python pi.py 1000000
    #         to throw 1000000 darts and report the estimate
    #   python pi.py 1000000 9
    #         to throw 1000000 darts, 9 times.
    #   python pi.py 1000000 9 > experiment_1000000_9.tsv
    #         to throw 1000000 darts, 9 times, and save results in a file
    parser = argparse.ArgumentParser()
    # The first command-line argument will be called "ndarts".
    # It's an integer, and is optional and will default to 1000
    parser.add_argument("ndarts", type=int, nargs="?", default=1000)
    # The second command-line argument will be called "experiments"
    # It's also an optional integer, and defaults to 1 if not specified
    parser.add_argument("experiments", type=int, nargs="?", default=30)
    args = parser.parse_args()
    # Now args is an object with fields .ndarts and .experiments
    # whose values are taken from the command line.

    # Run the experiments and report the results!
    for _ in range(args.experiments):
        approx = approximate(args.ndarts)
        print(approx, sep="\t")
