# Runtime Analysis of ```generate_rows(width)```

To arrive at a runtime of $O(n \cdot 1.32^n)$ for our generating rows function we can start by using a generating function. 

```python
    if width - 2 >= 0:
        rows.extend([row + [2] for row in generate_rows(width - 2)])

    if width - 3 >= 0:
        rows.extend([row + [3] for row in generate_rows(width - 3)])
```

This part of the function can be modeled by $a_{n} = a_{n-2} + a_{n-3}$ which we can now find and use a generating function for:

$$a_{n} = a_{n-2} + a_{n-3} \quad a_{0} = 0 \quad a_{1} = 1 \quad a_{2} = 1$$

$$Def A(x) = \sum_{n=0} a_{n}x^n$$