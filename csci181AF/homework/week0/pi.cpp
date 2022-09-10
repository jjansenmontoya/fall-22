#include <cstdlib>
#include <iostream>
#include <random>

// Usage (after compiling with make)
//
//   ./pi
//        To generate an approximation using the default 1000 points
//   ./pi 1000000
//        To generate an approximation using 1000000 points
//   ./pi 1000000 9
//        To generate an approximation using 1000000 points, 9 times

double approximate(long long npoints)
{
    // Get ready to generate some random numbers between 0 and 1,
    // without worrying too much about their quality.
    std::random_device randDev;
    std::mt19937 randGen(randDev());
    std::uniform_real_distribution<double> uniform_dist(0.0, 1.0);

    // Working with the function y = sqrt(1-x*x), pick a
    // bunch of x values, and calculate an average of
    // all the corresponding y values (by summing them
    // and dividing by the number of y values).
    double sum = 0.0;
    for (long long i = 0; i != npoints; ++i)
    {
        // Use the pseudorandom generator to pick a number
        // between 0 and 1
        double x = uniform_dist(randGen);
        double y = sqrt(1 - x * x);
        sum += y;
    }
    double average = sum / npoints;

    // The average function value should be pi/4;
    // multiply by 4 to get an approximation to pi.
    return 4.0 * average;
}

int main(int argc, char **argv)
{
    if (argc > 3)
    {
        // Too many command-line arguments. Print message and quit
        std::cout << "usage: " << argv[0] << "  <heapsize> [ <iterations> ]\n";
        return -1;
    }
    // If there's at least one argument (beside the name of the program which
    // is always argument 0), convert it from ascii string to integer and use it
    // as the number of points; otherwise, use 1000 points.
    long long npoints = (argc >= 2) ? atoi(argv[1]) : 1000;
    // If there's a third argument, convert it from ascii string to integer and
    // use it as the number of experiments; otherwise, run one experiment.
    long experiments = (argc == 3) ? atoi(argv[2]) : 1;

    // Don't round doubles when printing them.
    std::cout.precision(17);

    for (long expt = 0; expt != experiments; ++expt)
    {
        auto approx = approximate(npoints);
        std::cout << approx << "\n";
    }

    return 0; // Returning 0 from main means there was no error.
}