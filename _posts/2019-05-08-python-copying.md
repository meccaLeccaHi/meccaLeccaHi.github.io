---
title: "Shallow/Deep Copying in Python"
date: 2019-05-08
layout: post
math: false
category: blog
comments: true
tag:
- Python
- Pandas
author: adam
description: Demo on copying objects in Python.
---

I've been reading a great book that was recently gifted to me- [Math Adventures with Python](https://nostarch.com/mathadventures) by Peter Farrell. It contains a lot of fun exercises that convey rather technical mathematical concepts via relatively simple Python code. I thoroughly enjoyed it.

Among the subtler points made, is the following example, which I wanted to make available to my students. What follows is a brief demo on how to avoid getting "caught" by one of Python's more unique quirks - **_'shallow'_ vs. _'deep'_ copying of Python objects.**

---

As we can see below, Python objects exhibit some strange behaviors when duplicating existing variables.
- Let's declare a list variable and then set another variable to equal the first one.


```python
a = [1,2,3] # declare a list
b = a # set another variable equal to it
print(b)
```

    [1, 2, 3]


Then, let's change the value of the first variable.
- The second variable should be unaffected, _right?_


```python
a.append(4)
print(a)
print(b)
```

    [1, 2, 3, 4]
    [1, 2, 3, 4]


**Apparently not!**
As we can see above, by changing `a`, we unknowingly changed `b`, as well.
- This is because `a` and `b` are just names for the same object in your computer's memory.
- We are basically telling Python: "Assign this list to variables `a` and `b`".
> Like how 'William' and 'Bill' can refer to the same person.
---
Several solutions exist to this problem. One way to make sure that each variable is an entirely separate object, is to use **index notation**.
- We've seen how to use _indexing_ to slice arrays (e.g. `foo[4:10:2]`).
- We'll use the same notation to effectively tell Python: "Assign all the contents of list `a` to the variable `b`".


```python
a = [1,2,3]
b = a[::]
print(b)
a.append(4)
print(a)
print(b)
```

    [1, 2, 3]
    [1, 2, 3, 4]
    [1, 2, 3]


As we can see, the variables are no longer linked to each other.

**Just remember:** You can use index notation any time you want to avoid the object reference problem we saw here.

---

**DataFrames**, on the other hand, are handled _a bit differently_ when it comes to copying.

The same problem applies to DataFrame objects, as well -- we need to take precautions to not modify the source DataFrame. But, the solution is different.
- Instead of indexing, we use the `copy()` method to duplicate a DataFrame.
- Although, often it ends up being unnecessary, when performing interactive data exploration, it's better to be safe than sorry.


```python
# Python throws up a warning up when we try to operate on a shallow copy (to remind us of our misdeeds).
import pandas as pd

df = pd.DataFrame({'x': [1,2]}) # create DataFrame
df_sub = df[0:1] # subset DataFrame
df_sub.x = -1 # manipulate subset
```

    /anaconda3/envs/venv/lib/python3.6/site-packages/pandas/core/generic.py:4405: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      self[name] = value



```python
# The solution is simply to perform a deep copy, making them separate objects in the computer's memory.
df = pd.DataFrame({'x': [1,2]})
df_sub_copy = df[0:1].copy()
df_sub_copy.x = -1
print(df)
# No more warnings :)
```

       x
    0  1
    1  2


> For more info on shallow vs. deep copying, check out [this link](https://realpython.com/copying-python-objects/).
