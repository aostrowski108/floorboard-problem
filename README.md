# Floorboard Problem

## Problem description:
Consider building a floor out of $(2 \times 1)$ and $(3 \times 1)$ floorboards (length $\times$ width dimesions). For aesthetic reasons, the end of the boards should not line up. For example, the following $(9 \times 3)$ floor is not acceptable due to the alignment shown in red:
![Example Diagram](https://github.com/aostrowski108/floorboard-problem/blob/main/diagram.png)

There are eight ways of forming an acceptable $(9 \times 3)$ floor, expressed as $F(9,3) = 8$.

Calculate $F(32,10)$

## Solution
The solution to this problem involves an algorithm that uses simulation along with dynamic programming. Given that we are trying to find all acceptable ways of designing a floor of a specific height and width with an acceptable pattern, the first step is to find all possible rows that can be made of a given width. 

```python
def generate_rows(width):
    if width == 0:
        return [[]] 
    elif width == 1:
        return [] 

    rows = []
    if width - 2 >= 0:
        rows.extend([row + [2] for row in generate_rows(width - 2)])

    if width - 3 >= 0:
        rows.extend([row + [3] for row in generate_rows(width - 3)])
    return rows
```

This function works by taking in a width and then simulating by adding tiles with a width of either 2 and/or 3 until we reach a base case of 0 or 1. The reason our 0 base case returns ```[[]]``` is because this was we provide a way for the recursive calls to append floorboards (of lengths 2 or 3) to this empty combination. When ```width == 1```, the function returns []. This is because it's impossible to fill a width of 1 using only floorboards of lengths 2 and 3. Therefore, the function correctly returns an empty list, indicating that there are no possible rows for this width.
