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

$$A(x) := \sum_{n=0} a_{n}x^n$$

$$\sum_{n=3} a_{n} x^n = \sum_{n=3} a_{n-2} x^n + \sum_{n=3} a_{n-3} x^n$$

$$A(x) - a_{0} - a_{1}x - a_{2}x^2 = x^2[A(x) - a_{0}] + x^3A(x)$$

$$A(x) - x^2A(x) - x^3A(x) = x + x^2$$

$$A(x) = \frac{x+x^2}{1-x^2-x^3}$$

$$1 - x^2 - x^3 \quad \text{has roots:}$$

$$r_{1} = \frac{1}{3} \left(-1 + \left(\frac{1}{2} \left(25 - 3 \sqrt{69}\right)\right)^{\frac{1}{3}} + \left(\frac{1}{2} \left(25 + 3 \sqrt{69}\right)\right)^{\frac{1}{3}}\right)$$

$$c_{1} =  -\frac{1}{3} + \frac{1}{6}i \left(i + \sqrt{3}\right) \left(\frac{1}{2} \left(25 - 3\sqrt{69}\right)\right)^{\frac{1}{3}} - \frac{1}{6} \left(1 + i\sqrt{3}\right) \left(\frac{1}{2} \left(25 + 3\sqrt{69}\right)\right)^{\frac{1}{3}}$$

$$c_{2} = -\frac{1}{3} - \frac{1}{6} \left(1 + i\sqrt{3}\right) \left(\frac{1}{2} \left(25 - 3\sqrt{69}\right)\right)^{\frac{1}{3}} + \frac{1}{6}i \left(i + \sqrt{3}\right) \left(\frac{1}{2} \left(25 + 3\sqrt{69}\right)\right)^{\frac{1}{3}}$$

$$A = \frac{x+x^2}{(x-r_{1})(x-c_{1})(x-c_{2})} = \frac{B_{1}}{(x-r_{1})} + \frac{B_{2}}{(x-c_{1})} + \frac{B_{3}}{(x-c_{2})}$$ 

$$x+x^2 = B_{1}(x-r_{1})(x-c_{1}) + B_{2}(x-r_{1})(x-c_{2}) + B_{3}(x-r_{1})(x-c_{1})$$

$$B_{1} = \frac{r_{1} + r_{1}^2}{(r_{1} - c_{2})(r_{1}-c_{2})} \quad B_{2} = \frac{c_{1} + c_{1}^2}{(c_{1} - r_{1})(c_{1}-c_{2})} \quad B_{3} = \frac{c_{2} + c_{2}^2}{(c_{2} - r_{1})(c_{2}-c_{1})}$$

$$A(x) = \frac{B_{1}}{x-r_{1}} + \frac{B_{2}}{x-c_{1}} + \frac{B_{3}}{x-c_{2}} $$

$$= -\frac{B_{1}}{r_{1}}(\frac{1}{1 - \frac{x}{r_{1}}}) -\frac{B_{2}}{c_{1}}(\frac{1}{1 - \frac{x}{c_{1}}}) -\frac{B_{3}}{c_{2}}(\frac{1}{1 - \frac{x}{c_{2}}})$$

$$\sum_{n} (-\frac{B_{1}}{r_{1}}) \cdot (\frac{x}{r_{1}})^n \quad + \quad ...$$

