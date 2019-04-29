---
title: "What are random seeds?"
date: 2019-03-14
layout: post
math: true
category: blog
comments: true
tag:
- random functions
- pseudorandom
author: adam
description: Quick explanation as to why we use seeds with random functions.
---

{% include figure.html url="https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Sunflower_Seeds_Kaldari.jpg/1200px-Sunflower_Seeds_Kaldari.jpg" caption="Image source: wikipedia.com" width="40%" %}

---

#### Brace yourself: "Random" functions aren't really random.
They actually just pick from very long list of 'pseudo-random' numbers every time we use them. Fortunately for us, this list is so long that these functions behave 'more-or-less' randomly, which is sufficient for most peoples' needs. Although any given sample of numbers from these functions will look close to random, they were actually generated using a deterministic process.

As implied by the name, a random function's "seed" is an integer value describing where on this list that particular function starts selecting numbers from. This allows us to us random function in a more controlled fashion, particularly during development, than would otherwise be possible if our function returned a different value on every iteration (the default behavior). This allows us to focus on the behavior of the rest of our code during development.

Observe what happens when we use a random function `train_test_split` repeatedly without setting the seed number.
```python
import numpy as np
from sklearn.model_selection import train_test_split

a, b = np.arange(10).reshape((5, 2)), range(5)
train_test_split(a, b)
```

    [array([[4, 5],
            [2, 3],
            [6, 7]]), array([[0, 1],
            [8, 9]]), [2, 1, 3], [0, 4]]

```python
a, b = np.arange(10).reshape((5, 2)), range(5)
train_test_split(a, b)
```

    [array([[2, 3],
            [0, 1],
            [4, 5]]), array([[8, 9],
            [6, 7]]), [1, 0, 2], [4, 3]]

On the other hand - notice what happens when we set a seed for the same random function?

```python
a, b = np.arange(10).reshape((5, 2)), range(5)
train_test_split(a, b, random_state = 99)
```
    [array([[8, 9],
            [6, 7],
            [2, 3]]), array([[4, 5],
            [0, 1]]), [4, 3, 1], [2, 0]]

```python
a, b = np.arange(10).reshape((5, 2)), range(5)
train_test_split(a, b, random_state = 99)
```

    [array([[8, 9],
            [6, 7],
            [2, 3]]), array([[4, 5],
            [0, 1]]), [4, 3, 1], [2, 0]]

But, *of course*, this changes with a different seed.

```python
a, b = np.arange(10).reshape((5, 2)), range(5)
train_test_split(a, b, random_state = 12345)
```

    [array([[6, 7],
            [2, 3],
            [4, 5]]), array([[0, 1],
            [8, 9]]), [3, 1, 2], [0, 4]]

Why they are not truly random is outside the scope of this post and very likely won't matter in your case. But, take a look [here](http://en.wikipedia.org/wiki/Pseudorandom_number_generator) for more details.

*Got questions?* Leave 'em in the comments!
