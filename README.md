# Floorboard Problem

## Problem description:
Consider building a floor out of $(2 \times 1)$ and $(3 \times 1)$ floorboards (length $\times$ width dimesions). For aesthetic reasons, the end of the boards should not line up. For example, the following $(9 \times 3)$ floor is not acceptable due to the alignment shown in red:
![Example Diagram](https://github.com/aostrowski108/floorboard-problem/blob/main/diagram.png)

There are eight ways of forming an acceptable $(9 \times 3)$ floor, expressed as $F(9,3) = 8$.

Calculate $F(32,10)$

## Solution

### ```generate_rows(width)```
+ The solution to this problem involves an algorithm that uses simulation along with dynamic programming. Given that we are trying to find all acceptable ways of designing a floor of a specific height and width with an acceptable pattern, the first step is to find all possible rows that can be made of a given width. 

+ This function works by taking in a width and then simulating by adding tiles with a width of either 2 and/or 3 until we reach a base case of 0 or 1. By returning ```[[]]``` in the 0 base case, we provide a way for the recursive calls to append floorboards (of lengths 2 or 3) to this empty combination. By returning ```[]``` in the base case of 1, we ensure that it is an invalid combination and nothing will be appended.

+ The runtime of this function is $O(1.32^n)$ where $n = width$. An in-depth explanation on this here.

### ```generate_prefix_sum(row)```
+ Now that we have every possible combination of rows for a given width, we will create a prefix sum based off of the sum of the floorboards used so far. We store these into a set for the $O(1)$ look up time which we will utilize in ```generate_conflict_list(prefix_sums)```

+ The runtime of this is...

### ```generate_conflict_list(prefix_sums)```
+ Since we have every possible row as a prefix sum, we can calculate a list for all viable patterns that can be adjacent to the row. To do this, we will loop through every prefix sum and check if at any point the two sets are disjoint. If they are, we know that they are a viable adjacent pattern and add it to the list. We will do this for every prefix sum and return a list of lists.

+ The runtime of this algorithm $O(m^2 \c_dot n)$ where $m = len(prefix_sums)$ and $n = min(len(prefix_sums[i]), prefix_sums[j])$

### ```calculate_total_ways(conflict_list, height)```
+ 