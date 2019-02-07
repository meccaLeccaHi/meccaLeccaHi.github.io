---
title: "Iris Classification with Bayes Theorem"
date: 2018-11-14
layout: post
math: true
category: blog
comments: true
tag:
- Bayesian statistics
- iris database
- supervised classification
- machine learning
author: adam
description: A quick primer on Bayes' Theorem. 
---


# Applying Bayes' Theorem to Iris Classification
Can Bayes' theorem help us to solve a classification problem, namely predicting the species of an iris?

> See this excellent [discussion](https://www.youtube.com/watch?v=eDMGDhyDxuY) of Bayesian/frequentist approaches for greater background, if desired/required.

## Topic Guide
- [Learning Objectives](#learning-objectives)
- [Background](#background)
	- [Example: Medical Data](#example)
- [Preparing the Data](#preparing)
- [Deciding How to Make a Prediction](#prediction)
- [Calculating the Probability of Each Species](#calculating)
- [Summary](#summary)
- [Bonus: The Intuition Behind Bayes' Theorem](#bonus)


<a id="learning-objectives"></a>
## Learning Objectives

- Identify the types of problems Bayes Theorem is useful for.
- Observe an application of Bayes Theorem to example medical data.
- Determine how to apply Bayes Theorem to the prediction problem of your choosing.


<a id="background"></a>
## Background
{% include figure_link.html url="https://upload.wikimedia.org/wikipedia/commons/d/d4/Thomas_Bayes.gif" href="https://en.wikipedia.org/wiki/Thomas_Bayes" caption="Thomas Bayes (c. 1701 – 7 April 1761) Image source: wikipedia.com" width="40%" %}
From [*Wikipedia*](https://en.wikipedia.org/wiki/Thomas_Bayes): "Thomas Bayes was an English statistician, philosopher and Presbyterian minister who is known for formulating a specific case of the theorem that bears his name: [*Bayes' theorem*](https://en.wikipedia.org/wiki/Bayes%27_theorem). Bayes never published what would become his most famous accomplishment; his notes were edited and published after his death".

Wikipedia further explains that Bayes Theorem "describes the probability of an event, based on prior knowledge of conditions that might be related to the event. For example, if cancer is related to age, then, using Bayes' theorem, a person's age can be used to more accurately assess the probability that they have cancer, compared to the assessment of the probability of cancer made without knowledge of the person's age."

### Formula
Bayes' theorem is stated as the following equation:

$$P(A \ | \ B) = \frac {P(B \ | \ A) \times P(A)} {P(B)}$$

where $A$ and $B$ are events and $P(B) \ne 0$.

- $P(A \ | \ B)$ is a **conditional probability**: the likelihood of event $A$ occurring given that $B$ is true.

- $P(B \ | \ A)$ is also a conditional probability: the likelihood of event $B$ occurring given that $A$ is true.

- $P(A)$ and $P(B)$ are the probabilities of observing $A$ and $B$ independently of each other; this is known as the **marginal probability**.

<a id="example"></a>
> ### Example: Medical Data
Imagine a routine medical test that tests for a certain medical condition; influenza, for example. Pretend this test is 99% sensitive and 99% specific. In other words, the test will be positive produce 99% of the time for people with the disease and 99% true negative results for people without.
Now suppose that 0.5% of people have the disease. What is the probability that a randomly selected individual with a positive test has the disease?
>
> $$P(+_{Flu} \ | \ +_{Test}) = \frac {P(+_{Test} \ | \ +_{Flu}) P(+_{Flu})} {P(+_{Test})}$$
>
> $$ = \frac {P(+_{Test} \ | \ +_{Flu}) P(+_{Flu})} {P(+_{Test} \ | \ +_{Flu})P(+_{Flu})+P(+_{Test} \ | \ -_{Flu})P(-_{Flu})}$$
>
> $$ = \frac {0.99 \times 0.005} {0.99 \times 0.005 + 0.01 \times 0.995}$$
>
> $$ \approx 33.2\%$$

Now that we know how it works, can we use Bayes Theorem to help us to solve a classification problem, namely predicting the species of an iris?

<a id="preparing"></a>
## Preparing the Data

We'll read the iris data into a `DataFrame`, and round up all of the measurements to the next integer:


```python
import pandas as pd
import numpy as np
```

Read the iris data into a DataFrame.
```python
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


Apply the ceiling function to the numeric columns.
```python
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

<a id="prediction"></a>
## Deciding How to Make a Prediction

Let's say  I have an out-of-sample iris with the following measurements: 7, 3, 5, 2. How might I predict the species?

Show all observations with features 7, 3, 5, 2.
```python
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


Count the species for these observations.
```python
iris[(iris.sepal_length==7) & (iris.sepal_width==3) & (iris.petal_length==5) & (iris.petal_width==2)].species.value_counts()
```




    Iris-versicolor    13
    Iris-virginica      4
    Name: species, dtype: int64


Count the species for all observations.
```python
iris.species.value_counts()
```



    Iris-virginica     50
    Iris-versicolor    50
    Iris-setosa        50
    Name: species, dtype: int64



Let's frame this as a conditional probability problem: What is the probability of some particular species, given the measurements 7, 3, 5, and 2?

$$P(species \ | \ 7,3,5,2)$$

We could calculate the conditional probability for each of the three species, and then predict the species with the highest probability:

$$
	P(setosa \ | \ 7,3,5,2) \\
	P(versicolor \ | \ 7,3,5,2) \\
	P(virginica \ | \ 7,3,5,2)
$$

<a id="calculating"></a>
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

<a id="summary"></a>
## Summary

1. We framed a classification problem as three conditional probability problems.
2. We used Bayes' theorem to calculate those conditional probabilities.
3. We made a prediction by choosing the species with the highest conditional probability.

<a id="bonus"></a>
## Bonus: The Intuition Behind Bayes' Theorem

Let's make some hypothetical adjustments to the data to demonstrate how Bayes' theorem makes intuitive sense:

Pretend that more of the existing versicolors had measurements of 7,3,5,2, thus causing $P(7,3,5,2 \ | \ versicolor)$ to increase:
- This would result in increasing the numerator in Bayes' Theorem.
- So, given an iris with measurements of 7,3,5,2, the probability of it being a versicolor would be higher.

Pretend that most of the existing irises were versicolor:

- $P(versicolor)$ would increase, thus increasing the numerator in Bayes' Theorem again.
- So, the probability of any iris being a versicolor (regardless of measurements) would also increase.

Pretend that 17 of the setosas had measurements of 7,3,5,2:

- $P(7,3,5,2)$ would double, thus doubling the denominator.
- As a result, the probability of the same iris (with measurements of 7,3,5,2) being a versicolor would be cut in half.
