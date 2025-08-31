# heap_median

Given an input stream of `n` non-negative integers, perform the following task for each `i`th integer:

* Include the `i`th integer to a running collection of integers.
* Find the median of the updated integer collection.
* Print each median on a new line, each as a double-precision number scaled to 1 decimal place.

The reported median value depends on how many elements are in the collection.

* For an odd number of elements, the median would be the middle element if they were sorted.
* For an even number of elements, take the average of the two middle elements (if they were sorted).

## Function Description

Complete the runningMedian function which has the following parameters:

* `int a[n]`: an array of integers

Returns

* `str(float)[n]`: an array of strings formatting float values to 1 decimal place for each median.

## Input Format

The first line contains a single integer, `n`, the number of integers in the data stream.
Each line `i` of the `n` subsequent lines contains an integer, `a[i]`, to be inserted into the list.

## Constraints

* 1 <= n <= 10^5
* 0 <= a[i] <= 10^5
