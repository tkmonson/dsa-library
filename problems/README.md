# dsa-library: Problems

Welcome to my collection of solutions to DSA problems!

## Note on Auxiliary Space Complexity

**The term "auxiliary space" in these solutions is defined as the space the algorithm uses to compute the output, excluding the input and the output space.** If you are curious about the consequences of this choice, read on.

If we consider our model of computation to be a Turing machine with a read-only input tape and a write-only output tape, only the working tape the machine uses during computation is considered auxiliary space. However, these algorithms are being run on a RAM-based computer, where the input and output are stored in RAM along with auxiliary data structures, which leads to complications:

1. Some of these solutions use in-place algorithms, which modify the input space directly. By the above definition, for example, an in-place heapsort and a sorting algorithm that sorts elements from the input into a separate output array are both O(1). If an algorithm is in-place, that will be noted separately.

2. Some algorithms may use a very large output space and a much smaller auxiliary space, like an algorithm to compute all of the permutations of a set of integers. For such algorithms, output space will be noted separately.

3. In a multi-tape Turing machine, when a symbol is written to the output tape, it is final. On a RAM-based computer, an algorithm could define an "output array" (the array that is eventually returned), do work inside of it, and be considered O(1) because the output space does not count toward auxiliary space. This is "gaming" the auxiliary space complexity analysis based on exploitation of the above definition. Let's say you are building up an output array as the algorithm runs. Technically, if elements in the output array are ever read or modified after being appended, then it counts as auxiliary space because work is being done. If not, then the elements could conceivably be printed to the output tape as they are computed, and the output array would not count as auxiliary space.
