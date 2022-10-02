#include <algorithm> // std::accumulate, std::nth_element
#include <cassert>
#include <chrono>     // std::chrono::high_resolution_clock
#include <functional> // std::greater<T>(), std::less<T>()
#include <iostream>
#include <queue> // std::priority_queue<T>
#include <random>
#include <vector>

// ==================
// Helper functions //
// ==================

// For debugging purposes: print the contents of a vector.
//  (Hopefully a short vector, or you'll be generating a lot of output!)
template <typename T>
void dumpVec(const std::vector<T> &a)
{
    for (const auto &x : a)
    {
        std::cout << " " << x;
    }
    std::cout << "\n";
}

// Computes the average (arithmetic mean) of a vector
template <typename T>
double average(const std::vector<T> &a)
{
    double sum = std::accumulate(begin(a), end(a), 0.0);
    return sum / a.size();
}

// Computes the sample standard deviation of a vector of doubles.
//   Note: the result describes the range of the observed data;
//   not how confident we are that the sample average is
//    close to the "true" average.
template <typename T>
double stdDev(const std::vector<T> &a)
{
    double sumSquares = 0;
    double avg = average(a);

    for (int m : a)
    {
        double d = m - avg;
        sumSquares += d * d;
    }

    double s = sqrt(sumSquares / (a.size() - 1));
    return s;
}

// Returns the *integer* sum of the given vector of integers
unsigned long long sumVec(const std::vector<unsigned long> &v)
{
    return std::accumulate(begin(v), end(v), 0ULL);
}

// Convert nanoseconds to milliseconds
template <typename T>
double ns_to_ms(T t)
{
    return t / 1000000.0;
}

unsigned long long expectedSum(unsigned long long n, unsigned long long k)
{
    // We can predict the sum of the k largest numbers in
    //    the range 0..(n-1) inclusive
    // (i.e., the sum of the numbers (n-k)..(n-1) inclusive)
    return n * k - (k * k + k) / 2;
}

// ========================
// The k-of-n strategy code
// ========================

// Strategy 1: sort
std::vector<unsigned long> strategy1(std::vector<unsigned long> copy,
                                     size_t k)
{
    // We call the input "copy" because we're passing the parameter
    //   *by value*, which means we're given a copy of the original vector
    //   so we are free to modify that copy without affecting other experiments.

    // Sort the whole vector copy

    std::sort(copy.begin(), copy.end(), std::greater<unsigned long>());

    // Create a vector<unsigned long> named answers with the last k elements
    //   of the sorted vector.

    std::vector<unsigned long> answers(begin(copy), begin(copy)+k);

    // Return that vector.  (C++ will optimize and there's no run-time copy cost.)
    
    return answers;
}

// Strategy 2: Quick Select (a.k.a. nth_element)
std::vector<unsigned long> strategy2(std::vector<unsigned long> copy,
                                     size_t k)
{
    // See strategy1 for why the parameter is called "copy",
    // and how returning the answer wordemks.

    // In expected-linear time, do a partial-sort of the whole
    //   vector copy (from begin to end) so that
    //      (1) the element k from the end is the k-th largest value
    //      (2) all elements before that position are smaller (<=)
    //      (3) all elements after that position are larger (>=)
    std::nth_element(begin(copy), end(copy) - k, end(copy));

    // Return the last k elements of the shuffled vector
    std::vector<unsigned long> answers(end(copy) - k, end(copy));
    return answers;
}

// Strategy 3: Maxheap
std::vector<unsigned long> strategy3(const std::vector<unsigned long> &numbers,
                                     size_t k)
{
    // Note that this time we take the numbers by const reference,
    // because the constructor for priority_queue will itself
    // copy the given range of numbers (and heapify them in linear time).

    // Create a priority queue containing all the numbers in the given vector.

    std::priority_queue<unsigned long> maxheap(begin(numbers), end(numbers));

    // Pull out the k biggest elements into a vector<unsigned long>
    std::vector<unsigned long> answers;
    for (size_t i = 0; i < k; i++) {
        answers.push_back(maxheap.top());
        maxheap.pop();
    }
    // Return them!
    return answers;
}

// Strategy 4: Minheap
std::vector<unsigned long> strategy4(const std::vector<unsigned long> &numbers,
                                     unsigned long k)
{
    // Create a *minheap* out of the range consisting of the
    //   first k elements of the input vector.

    std::priority_queue<unsigned long, std::vector<unsigned long>, std::greater<unsigned long>> minheap(begin(numbers), begin(numbers)+4);

    // For each remaining element in the input vector, compare
    // them to the minimum of the minheap; if the new number is
    // bigger, remove the minimum of the heap and insert the new number.

    for (size_t index = 0; index < numbers.size(); ++index ) {
        if (numbers[index] > minheap.top()) {
            minheap.pop();
            minheap.push(numbers[index]);
        }
    }

    // Put the contents of the minheap into a vector<unsigned long> and return it.
    // We don't need the elements out in sorted order, but there's
    // no way to iterate over a C++ std::priority_queue except through
    // repeated popping.
    std::vector<unsigned long> answer;
    while(!minheap.empty()) {
        answer.push_back(minheap.top());
        minheap.pop();
    }

    return answer;
}

// ==================
// Main program
// ==================

// Note: design choices
//    Parameters n and k are of type size_t (probably 64 bit)
//    Values in the heap are unsigned long  (possibly 32 bit)
//    Times in nanoseconds are of type long long (probably 64 bit)

int main(int argc, char **argv)
{
    // Parse command-line arguments
    if (argc < 3 || argc > 4)
    {
        // Wrong number of command-line arguments. Print message and quit
        std::cout << "usage: " << argv[0] << "  <n> <k> [ <iterations> ]\n";
        return -1;
    }
    // Convert argument n from ascii string to a number (using base 10)
    size_t n = strtoul(argv[1], nullptr, 10);

    // Convert argument k from ascii string to a number (using base 10).
    size_t k = strtoul(argv[2], nullptr, 10);

    // Check that we're not asking for more numbers than we have.
    assert(k <= n);

    // If there's a final argument, convert it from ascii string to number and
    // use it as the number of experiments; otherwise, run one experiment.
    size_t experiments = (argc == 4) ? strtoul(argv[3], nullptr, 10) : 1UL;

    // Simplest code to get some randomness, not necessarily high quality
    std::random_device rd;
    std::mt19937 g(rd());

    // The vector of n numbers is just called "numbers"
    // It is initialized to the numbers 0..n-1 inclusive to start,
    // but we'll shuffle it later.
    std::vector<unsigned long> numbers(n);
    std::iota(numbers.begin(), numbers.end(), 0ul);

    // We'll declare t_start and t_stop to be abstract times.
    std::chrono::high_resolution_clock::time_point t_start, t_stop;

    // Run "experiements" iterations of each experiment/
    // We interleaving the different strategies for two reasons:
    //   (1) It's fairer to use the same shuffled numbers for each
    //       strategy, in case some shuffles are "easier" than others.
    //   (2) If we ran several iterations of the first strategy, and only then
    //       several iterations of the next strategy, external factors
    //       are more likely to affect one strategy more than the other.
    //       (e.g., the laptop gradually heats up, and at some point
    //        during the benchmarking the CPU decides to
    //        slow down its clock rate to avoid overheating)

    std::cout << "Strategy\tn\tk\ttime (ms)\n";

    for (size_t iteration = 0; iteration < experiments; ++iteration)
    {
        // Set numbers to be a random shuffle (of 0..n-1 inclusive)
        std::shuffle(numbers.begin(), numbers.end(), g);
        // Try the first strategy to extract the top k
        // -------------------------------------------

        t_start = std::chrono::high_resolution_clock::now();
        auto answers1 = strategy1(numbers, k);
        t_stop = std::chrono::high_resolution_clock::now();

        // Record the time difference (in nanoseconds) before and after
        long long time = std::chrono::duration<double, std::nano>(t_stop - t_start).count();
        // Check the answer, and that we didn't modify the given numbers
        assert(sumVec(answers1) == expectedSum(n, k));
        assert(sumVec(numbers) == static_cast<unsigned long long>(n) * (n - 1) / 2);
        // Display the result
        std::cout << 1 << "\t" << n << "\t" << k << "\t" << ns_to_ms(time) << "\n";

        // Try the second strategy to extract the top k
        // -------------------------------------------

        
        t_start = std::chrono::high_resolution_clock::now();
        auto answers2 = strategy2(numbers, k);
        t_stop = std::chrono::high_resolution_clock::now();

        // Record the time (in nanoseconds)
        time = std::chrono::duration<double, std::nano>(t_stop - t_start).count();
        // Check the answer, and that we didn't modify the given numbers
        assert(sumVec(answers2) == expectedSum(n, k));
        assert(sumVec(numbers) == static_cast<unsigned long long>(n) * (n - 1) / 2);
        // Display the result
        std::cout << 2 << "\t" << n << "\t" << k << "\t" << ns_to_ms(time) << "\n";
    

        // Try the third strategy to extract the top k
        // -------------------------------------------
        t_start = std::chrono::high_resolution_clock::now();
        auto answers3 = strategy3(numbers, k);
        t_stop = std::chrono::high_resolution_clock::now();

        // Record the time (in nanoseconts)
        time = std::chrono::duration<double, std::nano>(t_stop - t_start).count();
        // Check the answer, and that we didn't modify the given numbers
        assert(sumVec(answers3) == expectedSum(n, k));
        assert(sumVec(numbers) == static_cast<unsigned long long>(n) * (n - 1) / 2);
        // Display the result
        std::cout << 3 << "\t" << n << "\t" << k << "\t" << ns_to_ms(time) << "\n";

        // Try the fourth strategy to extract the top k
        // -------------------------------------------

        t_start = std::chrono::high_resolution_clock::now();
        auto answers4 = strategy4(numbers, k);
        t_stop = std::chrono::high_resolution_clock::now();

        // Record the time (in nanoseconds)
        time = std::chrono::duration<double, std::nano>(t_stop - t_start).count();
        // Check the answer, and that we didn't modify the given numbers
        assert(sumVec(answers4) == expectedSum(n, k));
        assert(sumVec(numbers) == static_cast<unsigned long long>(n) * (n - 1) / 2);
        // Display the result
        std::cout << 4 << "\t" << n << "\t" << k << "\t" << ns_to_ms(time) << "\n";
    }
}