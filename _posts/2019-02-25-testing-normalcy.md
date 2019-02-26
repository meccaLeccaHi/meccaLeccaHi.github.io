---
title: "Testing for Normalcy ('Is my data normal?')"
date: 2019-02-25
layout: post
math: true
category: blog
comments: true
tag:
- Normal distribution
- Pyplot
author: adam
description: A quick overview of the methods available for determining the normalcy of your data.
---

## Topic Guide
- [Testing for normalcy](#testing)
- [Graphical methods](#graphical)
- [Statistical tests](#statistical)


<a id="testing"></a>
### Testing for normalcy
In general, there are two types of normality tests.

- Graphical Methods:
These are methods for plotting the data and qualitatively evaluating whether the data looks Gaussian.
- Statistical Tests:
These are methods that calculate statistics on the data and quantify how likely it is that the data was drawn from a Gaussian distribution.

<a id="graphical"></a>
#### Option 1: Graphical methods
The informal approach to testing normality is to compare a histogram of the sample data to a normal probability curve. The empirical distribution of the data (the histogram) should be bell-shaped and resemble the normal distribution.


```python
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
plt.style.use('fivethirtyeight')

# This makes sure that graphs render in your notebook
%matplotlib inline
```


```python
dat_raw = np.random.randn(1000)

# Normalize raw data
dat_sorted = sorted(dat_raw)
dat_mean = np.mean(dat_raw)
dat_std = np.std(dat_raw)
dat_norm = (dat_sorted - dat_mean) / dat_std
dat_pdf = stats.norm.pdf(dat_norm)

# Plot data
f,ax1 = plt.subplots()
ax1.hist(dat_norm, 20, density=1) # Raw data first
ax1.plot(dat_norm , dat_pdf, lw=3, c='r') # Then overlay with normal distribution to compare
plt.show()
```


![png](/assets/images/normal/normal_curve.png)



```python
# Add some bias for next example
bias = np.random.randn(1000)
bias[bias<0]=0
dat_bias_raw = np.random.randn(1000)+bias*5

# Normalize raw data
dat_sorted = sorted(dat_bias_raw)
dat_mean = np.mean(dat_bias_raw)
dat_std = np.std(dat_bias_raw)
dat_norm = (dat_sorted - dat_mean) / dat_std
dat_pdf = stats.norm.pdf(dat_norm)

# Plot data
f,ax1 = plt.subplots()
ax1.hist(dat_norm, 20, density=1 ) # Raw data first
ax1.plot(dat_norm , dat_pdf, lw=3, c='r') # Then overlay with normal distribution to compare
ax1.set_xlim([-5,5])
plt.show()
```


![png](/assets/images/normal/skew.png)

<a id="statistical"></a>
#### Option 2: Statistical tests
There are many statistical tests that we can use to quantify whether a sample of data looks as though it was drawn from a Gaussian distribution.

Each test makes different assumptions and considers different aspects of the data. To interpret them, we use the standard hypothesis testing approach that we've seen previously.
>These tests assume that that a sample was drawn from a Gaussian distribution (i.e. the null hypothesis, or $H_0$). We assign a threshold level before-hand (called alpha or $\alpha$- typically 0.05), that is used to interpret the p-value as follows:
>
>- p <= alpha: reject H0, not normal.
>- p > alpha: fail to reject H0, normal.

To state that another way- *Larger p-value suggest that our sample was likely drawn from a Gaussian distribution.*


```python
# Shapiro-Wilk Test
from scipy.stats import shapiro

def normality_test(data):
    stat, p = shapiro(data)
    print('Statistics=%.3f, p=%.3f' % (stat, p))
    # interpret
    alpha = 0.05
    if p > alpha:
        print('Sample appears to be Gaussian (fail to reject H0)')
    else:
        print('Sample does not appear to be Gaussian (reject H0)')
        
normality_test(dat_raw)
normality_test(dat_bias_raw)
```

    Statistics=0.998, p=0.491
    Sample appears to be Gaussian (fail to reject H0)
    Statistics=0.893, p=0.000
    Sample does not appear to be Gaussian (reject H0)


<a id='additional-resources'></a>
> #### Additional resources
>
> - [https://machinelearningmastery.com/a-gentle-introduction-to-normality-tests-in-python/](https://machinelearningmastery.com/a-gentle-introduction-to-normality-tests-in-python/)
