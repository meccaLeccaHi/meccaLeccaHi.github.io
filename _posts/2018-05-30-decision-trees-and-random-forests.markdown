---
title: "Decision trees and random forests 🌲"
date: 2018-05-30
layout: post
tag:
- tutorial
- machine learning
category: blog
author: john
description: Theory behind decision trees and random forests
---

I recently finished a masters in electrical and computer engineering at the University of Iowa. For my masters thesis I trained random forest classifiers to distinguish between two types of optic disc swelling, [papilledema](https://en.wikipedia.org/wiki/Papilledema) and nonarteritic anterior ischemic optic neuropathy ([NAION](http://eyewiki.aao.org/Non-Arteritic_Anterior_Ischemic_Optic_Neuropathy_(NAION))), using shape information extracted from optical coherence tomography ([OCT](https://en.wikipedia.org/wiki/Optical_coherence_tomography)) images of the retina.

Below is an excerpt from one of the chapters from my thesis covering the theory behind classical decision trees and random forests. I hope my descriptions of the concepts here can be of some use to those hoping to better understand tree-based classification.

---

# Decision trees and random forests
This chapter first describes the theory behind random forest classifiers, then details the specific implementation of a classifier trained on retinal layer shapes derived from volumetric SD-OCT images. Finally, the results of the classifier are presented along with a brief discussion of the work.

Random forest classifiers are an ensemble learning method built from decision trees. Decision trees often follow the Classification and Regression Tree (CART) framework, and, as the name implies, can be used for either classification or regression tasks [1]. This thesis focuses solely on binary classification trees and will use the general term decision trees to refer specifically to binary classification trees. Random forests, along with other improvements which will be detailed in below, combine the outputs of many decision tree models in order to produce an output that is both more accurate and less sensitive to noise than traditional decision trees.

## Classical decision trees
Decision trees operate with a simple objective of partitioning a dataset into two categories using a sequence of binary "Yes" or "No" splits. Decision trees achieve this objective by sequentially identifying features on which to split the data into subsets that are more homogeneous than the current subset. For example, when diagnosing a fever, a decision tree may classify a patient as having or not having a fever by answering a series of Yes or No questions, such as "is the temperature greater than 100F?", "are the palms sweaty?", etc, and arriving at a classification of having or not having a fever. The process of training a decision tree determines which Yes or No questions to ask (i.e. which features to split on) and at what values to set each Yes/No threshold.

There are a few parameters to select while training the binary tree: which features do we split on? How do we determine the threshold for splitting? When do we stop splitting the data (i.e. stop adding nodes to the tree)? The first two questions can be addressed through the use of an impurity metric.

Impurity can be thought of as a measure of the heterogeneity of dataset; a set of data with an equal distribution of two classes would be highly impure. The [Gini impurity index](https://en.wikipedia.org/wiki/Decision_tree_learning#Gini_impurity), $$I(t)$$, is a common measure of impurity in random forests [2-4]:
\begin{align}
    I(t) = \sum_{m=1}^{M} P(\omega_m |t)(1-P(\omega_m|t))
\end{align}
where $$P(\omega_m |t)$$ is the probability of finding a point, $$\omega_m$$, from class $$m$$ in a subset $$X_t$$ and $$M$$ is the total number of classes. $$X_t$$ is the current set of points at node $$t$$, before the data are split into two purer subsets. The probability is approximated as
\begin{align}
    P(\omega_m |t) = \frac{N_t^m}{N_t}, m = 1,2,\ldots,M
\end{align}
where $$N_t^m$$ is the number of points from class $$m$$ in a potential new subset $$X_{tY}$$ and $$N_t$$ is the total number of points in $$X_t$$.

The Gini impurity is maximal when $$P(\omega_m \vert t)$$ is uniform. Decision trees identify the optimal feature and threshold at each split by iterating through each of the features, testing different threshold values, and picking the combination of feature and threshold that results in the biggest decrease in $$I(t)$$. By minimizing the Gini impurity, decision trees identify subsets of the data that will be maximally pure.

The third question, determining when to stop splitting the data, is typically addressed through a heuristic approach known as pruning [3]. It is difficult to stop training a tree at precisely the right point; stopping early would result in poor classification results and stopping too late may result in overfitting. One common practice is to allow the tree to grow to a large size -- potentially overfitting to the data -- and then removing nodes to balance prediction error and model complexity [3].

Decision trees provide a number of advantages over other standard classification techniques. If a tree remains small, its results are easily interpretable. Decision trees can be adapted for regression or classification. And in general, decision trees are computationally simple and quick to fit.

However, there are also a number of substantial disadvantages associated with decision trees. Compared to support vector machines and other ensemble techniques, decision trees have low accuracy and are highly sensitive to small changes in their training data [3]. Additionally, decision trees are only able to split data parallel to the feature axes and are forced to approximate diagonal lines as many horizontal and vertical splits [2]. Random forests improve substantially on both of the issues of accuracy and instability while making justifiable concessions in interpretability of the model.

## Improvements of random forests over classical decision trees
Random forests were introduced in 2001 by Breiman to address a number of shortcomings associated with traditional decision trees, such as low accuracy and high sensitivity to variations in training data [5]. Random forests use a bootstrapped ensemble of decision trees along with a random sampling of features during training to achieve good accuracy while remaining robust to noise [5]. Random forests are now widely used in a variety of disciplines and generally applicable to a number of problems [6,7].

Bagging (**b**ootstrap **agg**regating) refers to the practice of training multiple trees on random subsets (with replacement) of the training data with the intent of reducing variance in the final model [8]. The final output of the ensemble of classifiers is then typically determined through an averaging or winner-takes-all vote of the output of each tree [3].

Traditional bagging trains trees on distributions that are identically distributed but not necessarily independent. The variance of $$N$$ identically distributed random variables with variance $$\sigma$$ is $$\rho\sigma^2 + \frac{1-\rho}{N}\sigma^2$$, whereas the variance of an average of $$N$$ independent identically distributed random variables is $$\frac{1}{N}\sigma^2$$ [6]. Random forests attempt to achieve the smaller predictor variance by producing trees that are independent as well as identically distributed. This is achieved by randomly selecting a subset of features at each split of the data (i.e. tree node).

As the trees comprising a random forest are trained using bagging, which selects a random subset of data for each tree, it is possible to identify samples that were not included in the training of a given tree. These samples are referred to as out-of-bag (OOB) and can be treated like an internal test set to evaluate the model [6]. The OOB error estimate is the mean prediction error of a sample $$x_i$$ calculated from the trees which did not include $$x_i$$ in their subset of training data [5,6].

Random forests (and decision trees is general) lend themselves to straightforward calculation of feature importance. A common approach for calculating feature importance in random forests is to simply rank features based on their total reduction in the Gini impurity at each split node accumulated across each of the trees used to build the forest [6]. It is common practice to normalize the importance of all features to range from 0 to 1 or 0 to 100 [4].

## References
  1. L. Breiman, [*Classification and Regression Trees*](https://www.taylorfrancis.com/books/9781351460491), Wadsworth statistics/probability series. Wadsworth International Group, 1984.
  2. C. M. Bishop, [*Pattern Recognition and Machine Learning*](https://www.springer.com/us/book/9780387310732). Secaucus, NJ, USA: Springer-Verlag New York, Inc., 2006.
  3. S. Theodoridis, [*Machine Learning: A Bayesian and Optimization Perspective*](https://www.elsevier.com/books/machine-learning/theodoridis/978-0-12-801522-3), .NET Developers Series. Elsevier Science, 2015.
  4. F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau, M. Brucher, M. Perrot, and E. Duchesnay, [“Scikit-learn: machine learning in python,”](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) *Journal of Machine Learning Research*, vol. 12, pp. 2825–2830, 2011.
  5. L. Breiman, [“Random forests,”](https://link.springer.com/article/10.1023/A:1010933404324) *Machine Learning*, vol. 45, no. 1, pp. 5–32, 2001.
  6. T. Hastie, R. Tibshirani, and J. Friedman, [*The Elements of Statistical Learning*](https://web.stanford.edu/~hastie/Papers/ESLII.pdf), 12th printing, Springer Series in Statistics. New York, NY, USA: Springer New York Inc., 2017.
  7. J. Shotton, A. Fitzgibbon, M. Cook, T. Sharp, M. Finocchio, R. Moore, A. Kipman, and A. Blake, [“Real-time human pose recognition in parts from single depth images,”](https://ieeexplore.ieee.org/document/5995316) *CVPR* 2011, pp. 1297–1304, 2011.
  8. L. Breiman, [“Bagging predictors,”](https://link.springer.com/article/10.1023/A:1018054314350) *Machine Learning*, vol. 24, no. 2, pp. 123–140, 1996.
