---
title: "Measuring Baseline Accuracy"
date: 2018-11-10
layout: post
mathjax: true
category: blog
comments: true
tag:
- supervised classification
- classification
- regression
author: adam
description: A brief explanation on the rationale behind measuring a baseline accuracy score.
---

The purpose of this article is to highlight the importance of performing baseline measurements as a routine pre-cursor to evaluating the performance of your model(s). Although, the information provided by the baseline measurement is purely a conceptual one, it can help us avoid some very common pit-falls
in ML.

>Let's start with an example. Say you had a bag of 100 marbles (40 green, 15 orange, 25 blue, and 20 red), and you trained a statistical model to predict the color using a series of attributes carefully collected with expensive scientific equipment. 
>Without stopping to consider the baseline score that our model should be a capable of, we might assume that our classifier is succeeding if it guesses color correctly more than 25% (1 out 4 [colors]).
>However the more 'accurate' interpration of the true baseline accuracy (in this classification example), is the proportion of the most common prediction (e.g. 40%, corresponding to always guessing 'green' in our current example). 
>In general, we can see here how consistent use of baseline accuracy measurement, can provide us with more reasonable expectations, and help us interpret our findings more readily.

More broadly, the baseline is typically calculated in the following ways:
- Classification: As we saw in the previous example, with classification we select the class with the greatest number of observations and use it for all predictions. 
- Regression: Since we are trying to predict a continuous value, we simply take some form of the central tendency (mean or median) and use it for all predictions.

As you can probably see by now, in some ways, a bad baseline score can be a good thing, as it leaves your model with _lots_ of room for improvement.
