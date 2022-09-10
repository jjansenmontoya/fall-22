#include <cassert>
#include <cstddef>
#include <iostream>
#include <random>
#include <utility>
#include <vector>

// Where is the parent (if any) of the element at index i?
inline size_t parent(size_t i)
{
    return (i - 1) / 2;
}

// Where is the left child (if any) of the element at index i?
inline size_t left(size_t i)
{
    return 2 * i + 1;
}

// Where is the right child (if any) of the element at index i?
inline size_t right(size_t i)
{
    return 2 * i + 2;
}

// bubbleUp(a,i)
//    a is a vector representing a maxheap except that
//    the value a[i] might be too *big* and need to be moved
//    *closer* to the root.
template <typename T>
void bubbleUp(std::vector<T> &a, size_t i)
{
    // Sanity-check that we're bubbling an element that exists.
    assert(i < a.size());

    // Stop looping if we've bubbled all the way to the root (index 0)
    while (i != 0)
    {
        // Is a[i] in the right place? Let's look at the parent...
        // (which must exist because we wouldn't stil be looping if
        // we were already at the root.)
        size_t p = parent(i);
        if (a[i] > a[p])
        {
            // The parent's value is too small.
            // Swap the a[i] with the parent's value.
            std::swap(a[i], a[p]);
            // continue looping, but set i to the parent's location
            // so that the value we are bubbling up can still be found
            // at location a[i].
            i = p;
        }
        else
        {
            // The parent's value is at least as big as a[i],
            // so a[i] is in the right position for a maxheap.
            break;
        }
    }
    return;
}

// sinkDown(a,i)
//    a is a vector representing a maxheap except that the value a[i] might
//    be too *small* (smaller that at least one child) and might need to be
//    moved *further* from the root of the tree.
template <typename T>
void sinkDown(std::vector<T> &a, size_t i)
{
    // Sanity-check that we're sinking an element that exists.
    assert(i < a.size());

    while (true)
    {
        // We want c to be the index of the child with the larger value

        // Start by guessing the left child is larger
        size_t c = left(i); // The index of the left child, if any
                            // The right child will be at index c+1 in the array.
        if (c >= a.size())
            // Oops; there's no left child, so there can't be a right child
            // (because a heap is a complete tree), so there aren't any
            // children at all. That means a[i] is a leaf and can't be moved
            // any further from the root!
            break;
        if (c < a.size() - 1 && a[c] < a[c + 1])
            // If a right child exists, and it's larger than the
            // left child, then our guess was wrong and we make
            // c be the index of the right child.
            c += 1;

        // c is now the index of the smaller child

        if (a[i] < a[c])
        {
            // a[i] is not bigger than its children, so we have a
            // violation of the maxheap property. Swap a[i]
            // with its larger child
            std::swap(a[i], a[c]);
            // And update i so that the value we are moving downwards
            // can still be found at location a[i].
            i = c;
        }
        else
        {
            // a[i] is bigger than its larger child, so it
            // is in the correct location for a maxheap.
            // Quit the loop because we're done moving a[i] around.
            break;
        }
    }
    return;
}

// Check whether the given array is in maxheap-order
template <typename T>
void assertMaxheap(const std::vector<T> &a)
{
    for (size_t i = 1; i < a.size(); ++i)
    {
        assert(a[i] <= a[parent(i)]);
    }
    return;
}

// Heapify the given vector using the top-down algorithm.
template <typename T>
void heapify_topdown(std::vector<T> &a)
{
    // TODO  (2-5 lines of code)
    return;
}

// Heapify the given vector using the bottom-up algorithm.
template <typename T>
void heapify_bottomup(std::vector<T> &a)
{
    // TODO  (2-6 lines of code)
    return;
}

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

//
// MAIN PROGRAM
//

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
    // as the number of heap elements. otherwise, use 1000.
    long long heapsize = (argc >= 2) ? atoi(argv[1]) : 1000;

    // If there's a third argument, convert it from ascii string to integer and
    // use it as the number of experiments; otherwise, run one experiment.
    long experiments = (argc == 3) ? atoi(argv[2]) : 1;

    // Create a random vector of unsigned longs,
    // and fill it with the numbers 0...heapsize-1
    std::vector<unsigned long> a0(heapsize);
    std::iota(a0.begin(), a0.end(), 0);

    // Simplest code to get some random numbers.
    std::random_device rd;
    std::mt19937 g(rd());

    for (int i = 0; i < experiments; ++i)
    {
        // Randomly shuffle the numbers 0...heapsize-1
        std::cerr << "shuffling the starting array...\n";
        std::shuffle(a0.begin(), a0.end(), g);
        std::cerr << "done\n";
        // dumpVec(a0)

        // Heapify a copy of the numbers using the top-down method
        std::cerr << "copy 1...\n";
        auto a1 = a0;
        std::cerr << "top_down heapify...\n";
        heapify_topdown(a1);
        // dumpVec(a1)
        std::cerr << "checking heap order...\n";
        assertMaxheap(a1);
        std::cerr << "done\n";

        // Heapify a copy of the numbers using the bottom-up method
        std::cerr << "copy 2...\n";
        auto a2 = a0; // Use the same random array
        std::cerr << "bottom_up heapify...\n";
        heapify_bottomup(a2);
        // dumpVec(a2)
        std::cerr << "checking heap order...\n";
        assertMaxheap(a2);
        std::cerr << "done\n";
    }

    std::cout << "The End\n";
}