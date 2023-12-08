# Floorboard Problem

## Problem description:
Consider building a floor out of $(2 \times 1)$ and $(3 \times 1)$ floorboards (length $\times$ width dimesions). For aesthetic reasons, the end of the boards should not line up. For example, the following $(9 \times 3)$ floor is not acceptable due to the alignment shown in red:
![Example Diagram](https://github.com/aostrowski108/floorboard-problem/blob/main/diagram.png)

There are eight ways of forming an acceptable $(9 \times 3)$ floor, expressed as $F(9,3) = 8$.

Calculate $F(32,10)$

## Solution
The solution to this problem involves an algorithm that uses simulation along with dynamic programming. Given that we are trying to find all acceptable ways of designing a floor of a specific height and width with an acceptbale pattern, the first step is to find all possible rows that can be made of a given width. 

```python
# This is a Python code block
def hello_world():
    print("Hello, World!")

hello_world()
```
