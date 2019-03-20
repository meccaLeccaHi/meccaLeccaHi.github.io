---
title: "Understanding Unpacking"
date: 2019-03-20
layout: post
math: false
category: blog
comments: true
tag:
- multiple assignment 
- tuple unpacking
author: adam
description: Short primer on how to use unpacking in Python.
---

# Understanding Unpacking

{% include figure.html url="https://upload.wikimedia.org/wikipedia/commons/b/b1/Von_baer_milan_leather_travel_bag.jpg" caption="Image source: wikipedia.com" width="40%" %}

---

*'Unpacking'* in itself allows us to break down the contents of an object and assign them to several variables simultaneously. Although, this feature may seem simple after you've already learned about it, it can be a little tricky to recall multiple assignment syntax when you need it most.

#### Let's create a packed object (boxed), then unpack it using a `for` loop.


```python
# Let's start with two lists that are related in some manner:
package = ['package_1','package_2','package_3','package_4']
directions = ['directions_1','directions_2','directions_3','directions_4']

# We'll zip them together to form the pairs.
# We can then use `for Obj-1, Obj-2 in` to isolate the values we need.
for p, d in zip(package, directions):
    print('Shipment: {} | Shipment Contents: {}'.format(p,d))
```

    Shipment: package_1 | Shipment Contents: directions_1
    Shipment: package_2 | Shipment Contents: directions_2
    Shipment: package_3 | Shipment Contents: directions_3
    Shipment: package_4 | Shipment Contents: directions_4


Rather than using a `for` loop to unpack an output, we can simply assign the results, assuming we know exactly how many results need to be assigned. 
- We can think of the result of `zip` as comprising four subcomponents; we can use a `for` loop to help us break the subcomponents out *OR* use the unpacking method (shown below).


```python
# Unpack output from zip into four variables:
box1, box2, box3, box4 = zip(package, directions)

# Check out contents of a few:
print(box1)
print(box3)
```

    ('package_1', 'directions_1')
    ('package_3', 'directions_3')


Naturally, we can use unpackaging assignment with the return value of a function, as exemplified below.


```python
# Create a function that takes an argument to act up. 
def min_max(nums):
    smallest = min(nums)
    largest = max(nums)
    
    # The function returns a list in the order below.
    return [smallest, largest, 5]
```


```python
# We can assign the returned list to a single variable,
min_and_max = min_max([1, 2, 3])

print(min_and_max)
print(type(min_and_max))
```

    [1, 3, 5]
    <class 'list'>



```python
# OR, because we know the list is composed of three elements, 
# assign each element to its own variable.
the_min, the_max, five = min_max([1, 2, 3])

print(the_max)
print(the_min)
print(five)
```

    3
    1
    5

*Any questions?* Leave 'em in the comments!

