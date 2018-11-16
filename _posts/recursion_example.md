
### [Recursion](https://en.wikipedia.org/wiki/Recursion) example

<img src='https://imgs.xkcd.com/comics/fixing_problems.png' style="float: center; height: 250px">
Source: [xkcd.com](https://imgs.xkcd.com/comics/fixing_problems.png)

The most common example people use to describe recursion involves the [factorial function](https://en.wikipedia.org/wiki/Factorial). 

$$5! = 5*4*3*2*1 = 120$$

Imagine struggling to create a custom function to do this with any positive number. As we can see below, we can implement the factorial in Python easily and elegantly using recursion.


```python
def factorial(n):
    #print(n)
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
factorial(5)
```




    120



In general, recursion can be pretty opaque. But, we can get a clearer picture of what's happening inside our function from the example below.


```python
factorial(4)                   # = 24
4 * factorial(3)               # = 24
4 * 3 * factorial(2)           # = 24
4 * 3 * 2 * factorial(1)       # = 24
4 * 3 * 2 * 1                  # = 24
4 * 3 * 2                      # = 24
4 * 6                          # = 24
24                             # = 24
```




    24



**Pros:**
- Recursive functions make the code look neat and clean.
- A complex task can be performed more elegantly by breaking it down into more manageable parts using recursion.

**Cons:**
- Following the logic behind recursion can be challenging. As a result, recursive functions are often hard to debug.
- Recursive calls can be computationally expensive (inefficient) as they can take up a lot of space in memory.


```python
# A more advanced example using strings
def string_flipper(string):
    if string == "":
        return string
    else:
        return string[-1] + string_flipper(string[:-1])
    
string_flipper('worcestershire')
```




    'erihsretsecrow'


