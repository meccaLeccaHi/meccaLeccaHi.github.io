---
title: "Iris Classification with Bayes Theorem"
date: 2018-11-14
layout: post
math: true
category: blog
comments: true
tag:
- bayesian statistics
- supervised classification
author: adam
description: A quick primer on Bayes' Theorem. 
---


# Applying Bayes' Theorem to Iris Classification

[**Background Materials**](https://www.youtube.com/watch?v=eDMGDhyDxuY)- an excellent discussion of Bayesian/frequentist approaches

Can Bayes' theorem help us to solve a classification problem, namely predicting the species of an iris?

## Preparing the Data

We'll read the iris data into a `DataFrame`, and round up all of the measurements to the next integer:


```python
import pandas as pd
import numpy as np
```


```python
# Read the iris data into a DataFrame.
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
col_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']
iris = pd.read_csv(url, header=None, names=col_names)
iris.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Apply the ceiling function to the numeric columns.
iris.loc[:, 'sepal_length':'petal_width'] = iris.loc[:, 'sepal_length':'petal_width'].apply(np.ceil)
iris.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>6.0</td>
      <td>4.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>5.0</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5.0</td>
      <td>4.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5.0</td>
      <td>4.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>4.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>Iris-setosa</td>
    </tr>
  </tbody>
</table>
</div>



## Deciding How to Make a Prediction

Let's say  I have an out-of-sample iris with the following measurements: 7, 3, 5, 2. How might I predict the species?


```python
# Show all observations with features 7, 3, 5, 2.
iris[(iris.sepal_length==7) & (iris.sepal_width==3) & (iris.petal_length==5) & (iris.petal_width==2)]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sepal_length</th>
      <th>sepal_width</th>
      <th>petal_length</th>
      <th>petal_width</th>
      <th>species</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>54</th>
      <td>7.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>Iris-versicolor</td>
    </tr>
    <tr>
      <th>58</th>
      <td>7.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>Iris-versicolor</td>
    </tr>
    <tr>
      <th>63</th>
      <td>7.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>Iris-versicolor</td>
    </tr>
    <tr>
      <th>68</th>
      <td>7.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>Iris-versicolor</td>
    </tr>
    <tr>
      <th>72</th>
      <td>7.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>Iris-versicolor</td>
    </tr>
    <tr>
      <th>73</th>
      <td>7.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>Iris-versicolor</td>
    </tr>
    <tr>
      <th>74</th>
      <td>7.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>Iris-versicolor</td>
    </tr>
    <tr>
      <th>75</th>
      <td>7.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>Iris-versicolor</td>
    </tr>
    <tr>
      <th>76</th>
      <td>7.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>Iris-versicolor</td>
    </tr>
    <tr>
      <th>77</th>
      <td>7.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>Iris-versicolor</td>
    </tr>
    <tr>
      <th>87</th>
      <td>7.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>Iris-versicolor</td>
    </tr>
    <tr>
      <th>91</th>
      <td>7.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>Iris-versicolor</td>
    </tr>
    <tr>
      <th>97</th>
      <td>7.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>Iris-versicolor</td>
    </tr>
    <tr>
      <th>123</th>
      <td>7.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>126</th>
      <td>7.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>127</th>
      <td>7.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>Iris-virginica</td>
    </tr>
    <tr>
      <th>146</th>
      <td>7.0</td>
      <td>3.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>Iris-virginica</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Count the species for these observations.
iris[(iris.sepal_length==7) & (iris.sepal_width==3) & (iris.petal_length==5) & (iris.petal_width==2)].species.value_counts()
```




    Iris-versicolor    13
    Iris-virginica      4
    Name: species, dtype: int64




```python
# Count the species for all observations.
iris.species.value_counts()
```




    Iris-virginica     50
    Iris-versicolor    50
    Iris-setosa        50
    Name: species, dtype: int64



Let's frame this as a conditional probability problem: What is the probability of some particular species, given the measurements 7, 3, 5, and 2?

$$P(species \ | \ 7,3,5,2)$$

We could calculate the conditional probability for each of the three species, and then predict the species with the highest probability:

$$P(setosa \ | \ 7,3,5,2)$$
$$P(versicolor \ | \ 7,3,5,2)$$
$$P(virginica \ | \ 7,3,5,2)$$

## Calculating the Probability of Each Species

Bayes' theorem gives us a way to calculate these conditional probabilities.

Let's start with versicolor:

$$P(versicolor \ | \ 7,3,5,2) = \frac {P(7,3,5,2 \ | \ versicolor) \times P(versicolor)} {P(7,3,5,2)}$$

We can calculate each of the terms on the right side of the equation:

$$P(7,3,5,2 \ | \ versicolor) = \frac {13} {50} = 0.26$$

$$P(versicolor) = \frac {50} {150} = 0.33$$

$$P(7,3,5,2) = \frac {17} {150} = 0.11$$

Therefore, Bayes' theorem says the probability of versicolor given these measurements is:

$$P(versicolor \ | \ 7,3,5,2) = \frac {0.26 \times 0.33} {0.11} = 0.76$$

Let's repeat this process for virginica and setosa:

$$P(virginica \ | \ 7,3,5,2) = \frac {0.08 \times 0.33} {0.11} = 0.24$$

$$P(setosa \ | \ 7,3,5,2) = \frac {0 \times 0.33} {0.11} = 0$$

We predict that the iris is a versicolor, since that species had the highest conditional probability.

## Summary

1. We framed a classification problem as three conditional probability problems.
2. We used Bayes' theorem to calculate those conditional probabilities.
3. We made a prediction by choosing the species with the highest conditional probability.

## Bonus: The Intuition Behind Bayes' Theorem

Let's make some hypothetical adjustments to the data to demonstrate how Bayes' theorem makes intuitive sense:

Pretend that more of the existing versicolors had measurements of 7,3,5,2:

- $P(7,3,5,2 \ | \ versicolor)$ would increase, thus increasing the numerator.
- It would make sense that, given an iris with measurements of 7,3,5,2, the probability of it being a versicolor would also increase.

Pretend that most of the existing irises were versicolor:

- $P(versicolor)$ would increase, thus increasing the numerator.
- It would make sense that the probability of any iris being a versicolor (regardless of measurements) would also increase.

Pretend that 17 of the setosas had measurements of 7,3,5,2:

- $P(7,3,5,2)$ would double, thus doubling the denominator.
- It would make sense that given an iris with measurements of 7,3,5,2, the probability of it being a versicolor would be cut in half.
