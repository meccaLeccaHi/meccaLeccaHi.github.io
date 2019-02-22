---
title: "Introduction to the Normal Distibution and the Z-Score"
date: 2019-02-21
layout: post
math: true
category: blog
comments: true
tag:
- Normal distribution
- Z-score
author: adam
description: A brief intro to the wonders of the normal distribution and how we can use it to our advantage.
---

## Topic Guide
- [Learning Objectives](#learning-objectives)
- [Sample statistics and population parameters](#background)
- [The normal distribution](#normal)
- [The 68-95-99.7 Rule](#zdist-rule)
- [The z-score](#z-score)


<a id="learning-objectives"></a>
### Learning Objectives
- Understand the normal distribution and the concept of normality
- Visualize the normal distribution
- Understand the uses of the 68-95-99.7 Rule and the z-score
- Visualize the 69-95-99.7 Rule
- Apply z-scoring to data


```python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

%matplotlib inline
```

<a id='background'></a>

### Background: Sample statistics and population parameters

---

Recall that we use sample statistics to estimate population parameters. Our goal is to calculate sample statistics and then rely on properties of a random sample (and perhaps additional assumptions) to be able to make inferences that we generalize to the larger population of interest.

Below is a table comparing some example sample statistics and population parameters:

Metric  | Statistic  | Parameter 
------------- | --------------- | -------------
mean   | $$\bar{x} = \frac{\sum x}{n}$$ | $$ \mu = \frac{\sum x}{N} $$ 
variance | $$ s^2 = \frac{\sum_i (x_i - \bar{x})^2}{n-1} $$ | $$ \sigma^2 = \frac{\sum_i (x_i - \mu)^2}{N}  $$
standard deviation   | $$ s = \sqrt{\frac{\sum_i (x_i - \bar{x})^2}{n-1}} $$ | $$ \sigma = \sqrt{\frac{\sum_i (x_i - \mu)^2}{N} } $$

<a id='normal'></a>
### The normal distribution

---

Almost anyone reading this as probably heard of the *normal distribution* at one time or another. It's (arguably) the most frequently-utilized distribution in all of statistics. 
- **Normality** is an assumption that underlying many of common statistical tests and serves as a powerful tool for modeling the distribution of many variables that exist in nature.

The normal distribution is parameterized by two measures: 
- the population mean
- the population standard deviation

> If a variable is distributed in an *perfectly* normal distribution, its mean, median, and mode will all be equal.

**Example: Intelligence Quotient**

Intelligence Quotient (IQ) follows a normal distribution by design. IQ is normally distributed with a mean of 100 and a standard deviation of 15. You could see this described in the following way:
- IQ ~ Normal(100,15) 
- or IQ ~ N(100,15)

**We can plot the normal distribution N(100, 15) using scipy.**


```python
# generate points on the x-axis
xpoints = np.linspace(40, 160, 500)

# use stats.norm.pdf to get values on the probability density function for the normal distribution
ypoints = stats.norm.pdf(xpoints, 100, 15)

# initialize a matplotlib figure
fig, ax = plt.subplots(figsize=(8,5))

# plot the lines using matplotlib's plot function
ax.plot(xpoints, ypoints, linewidth=3, color='darkred');
```


![png](/assets/images/normal/normal_line.png)


<a id='zdist'></a>
### The 68-95-99.7 Rule

---

One of the primary benefits of the normal distributions is it's utility in helping us identify how extreme (or far away from the expected value) a particular observation is within the context of a distribution, both quickly and easily. 

> For **example:** 
> - An extreme stock price might indicate a major shift in the market. This might inform whether we choose to buy or sell. 
> - An extreme drop in air pressure might indicate a significant weather event, necessitating a reaction from the National Weather Service. 

Quantifying just how extreme a particular observation is from the expected value (a.k.a. population mean) may indicate a particular action we should take.

It is possible to show that, for a normal distribution:
- 68% of observations from a population will fall within $\pm 1$ standard deviation of the population mean
- 95% of observations from a population will fall within $\pm 2$ standard deviations of the population mean
- 99.7% of observations from a population will fall within $\pm 3$ standard deviations of the population mean

**Ask yourself:** 

1. What percentage of individuals have an IQ between 85 and 115?

1. What percentage of individuals have an IQ above 100?

1. What percentage of individuals have an IQ between 85 and 130?

**Below is a visual representation of the 68-95-99.7 Rule**
(using the IQ example)**:**


```python
# define mean and standard deviation
mu, sigma = 100, 15

# create a set of points
xpoints=np.random.normal(mu, sigma, 50000)

# measure stats
avg=np.mean(xpoints)
std=np.std(xpoints)

# check your values
print(avg,std)

# define variables for 1,2,3 sigma
std1 = avg + std
std1_neg = avg - std
std2 = avg + 2*std
std2_neg = avg - 2*std
std3 = avg + 3*std
std3_neg = avg - 3*std

## create figure
# initialize a matplotlib figure
fig, ax = plt.subplots(figsize=(8,5))

# 68%
ax.axvline(std1_neg, ls='dashed', lw=3, color='#333333', alpha=0.7)
ax.axvline(std1, ls='dashed', lw=3, color='#333333', alpha=0.7)

# 95%
ax.axvline(std2_neg, ls='dashed', lw=3, color='#666666', alpha=0.7)
ax.axvline(std2, ls='dashed', lw=3, color='#666666', alpha=0.7)

# 99.7%
ax.axvline(std3, ls='dashed', lw=3, color='#999999', alpha=0.7)
ax.axvline(std3_neg, ls='dashed', lw=3, color='#999999', alpha=0.7)

# plot the lines using matplotlib's hist function:
ax.hist(xpoints, density=True, bins=100)
plt.show();
```

100.01642077520381 14.989875844632797


![png](/assets/images/normal/normal_hist.png)


<a id='z-score'></a>
### The z-score

---

While it's nice to have this 68-95-99.7 rule, we can get *more specific.*

*The **z-score** of an observation quantifies **how many standard deviations the observation is away from the population mean**:*

### $$ z_i = \frac{x_i - \text{population mean of x}}{\text{standard deviation of x}} $$

> If we have **X ~ N(mu, sigma)**, with the random variable X specified by a normal distribution with mean mu and standard deviation sigma, we can specify the Z-distribution as  **Z ~ N(0,1)**. 
> 
> We call this particular Z the **standard normal distribution** because it has a mean of 0 and standard deviation of 1.

The `scipy.stats.zscore` function will convert a vector of values to their respective z-scores.

**Let's calculate the z-scores for a single vector of values...**


```python
import numpy as np
from scipy import stats

values = np.array([2,3,4,5,6])

stats.zscore(a)
```
    array([-1.41421356, -0.70710678,  0.        ,  0.70710678,  1.41421356])

**Ask yourself:** 
- What is the `scipy.stats.zscore` function doing to convert the vector of values?

<a id='additional-resources'></a>
> #### Additional resources
>
> - http://blog.vctr.me/posts/central-limit-theorem.html
>
> - http://www.usablestats.com/lessons/central_limit


