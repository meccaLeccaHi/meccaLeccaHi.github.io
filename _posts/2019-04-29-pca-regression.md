---
title: "Dimensionality Reduction with PCA"
date: 2019-04-29
layout: post
math: false
category: blog
comments: true
tag:
- principal components analysis
- dimensional reduction
- linear regression
- feature selection
author: adam
description: Demo on using unsupervised algos with supervised algos.
---

Principal components analysis (PCA) is one of the most popular methods available for reducing the number of variables in a data set.
- We typically describe PCA as an unsupervised learning tool.
- But, dimensionality reduction techniques are useful for supervised learning, too.
> In this article, we describe its use as a dimensional reduction step for linear regression.

---

We know that we can use linear regression to model the relationship between our dependent variable and one (or more) independent variables (i.e. 'features').
- Let's try using the principal components (the dimensions along which the data vary the most) as the features of our logistic regression and see how it affects our accuracy.


```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn import datasets

%matplotlib inline
```


```python
# load the diabetes dataset
data = datasets.load_diabetes()
```


```python
scaler = StandardScaler()

# define X
feature_matrix = pd.DataFrame(data.data, columns=data.feature_names)
scaled_feature_matrix = pd.DataFrame(scaler.fit_transform(data.data), columns=data.feature_names)

# define y
labels = data.target
```

Visualize correlations in raw data using `PairGrid`.


```python
g = sns.PairGrid(scaled_feature_matrix)
g = g.map_lower(sns.regplot)
g = g.map_upper(sns.kdeplot, cmap="Blues", shade=True, shade_lowest=False)
g = g.map_diag(plt.hist)

plt.show()
```

![png](/assets/images/pca_regression/output_6_0.png)


```python
# check linear regression scores before modifying data
linreg = LinearRegression()
orig_lr_scores = cross_val_score(linreg, scaled_feature_matrix, labels, scoring='neg_mean_squared_error', cv=25)

print(np.sqrt(-(orig_lr_scores).mean()))
```

    54.827882004879235


```python
# extract principal components 

# if not specified: n_components = min(n_samples, n_features)
# thus, in this case, n_components = 10, since n_features = 10
pca = PCA(n_components=4)
pca.fit(scaled_feature_matrix)
pca
```

    PCA(copy=True, iterated_power='auto', n_components=4, random_state=None,
      svd_solver='auto', tol=0.0, whiten=False)


Now, let's look at the principal component weighting vectors (i.e. eigenvectors).
- The principal components, or eigenvectors, can be thought of as weightings on the original variables to transform them into the new feature space.


```python
pc_names = [f'PC{i+1}' for i in range(len(pca.components_))]
```


```python
print(feature_matrix.columns)
for i, pc in enumerate(pc_names):
    print(pc, 'weighting vector:', pca.components_[i], '\n')
```

    Index(['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6'], dtype='object')
    PC1 weighting vector: [ 0.21643101  0.18696711  0.3031625   0.2717397   0.34325493  0.35186062
     -0.28243639  0.42883325  0.37861731  0.32218282] 
    
    PC2 weighting vector: [ 0.04437151 -0.38654811 -0.15628061 -0.13825564  0.57302669  0.45593985
      0.50624287 -0.06818423 -0.0261893  -0.0849466 ] 
    
    PC3 weighting vector: [ 0.49466811 -0.10685833  0.1675317   0.51356804 -0.0685867  -0.26969438
      0.38602787 -0.38068121  0.0636315   0.27684271] 
    
    PC4 weighting vector: [-0.4140095  -0.67986052  0.49982533 -0.01966734 -0.06839533 -0.16777384
     -0.07602005  0.0079212   0.26442742  0.08708624] 
    

Transform the original data into the principal component space.


```python
feat_mat_pcs = pd.DataFrame(pca.transform(scaled_feature_matrix), columns=pc_names)
```

Visualize correlations in PC's using [`PairGrid`](https://seaborn.pydata.org/generated/seaborn.PairGrid.html).
- Confirm that correlations between variables have been eliminated.


```python
g = sns.PairGrid(feat_mat_pcs)
g = g.map_lower(sns.regplot)
g = g.map_upper(sns.kdeplot, cmap="Blues", shade=True, shade_lowest=False)
g = g.map_diag(plt.hist)

plt.show()
```

![png](/assets/images/pca_regression/output_15_0.png)


```python
# now, check linear regression scores for the reduced data
linreg = LinearRegression()
pc_lr_scores = cross_val_score(linreg, feat_mat_pcs, labels, scoring='neg_mean_squared_error', cv=25)

print(pc_lr_scores)
print(np.sqrt(-(pc_lr_scores).mean()))
```

    [-2027.6628549  -3019.15010137 -3607.2529438  -2985.69406929
     -3180.22323011 -3764.00700745 -3016.33558951 -2387.44557416
     -3072.24575352 -1992.68736017 -2976.20060529 -4434.80564059
     -2687.61576252 -2495.19859718 -2597.20645699 -4756.32066251
     -3925.9488112  -2161.37263274 -2980.5194341  -2139.86955025
     -3947.14620781 -5444.70088653 -2341.69981362 -1849.4541157
     -2163.85541312]
    55.119731158422624


In the end, we arrived at a model with very similar performance to the larger model, but with the number of features greatly reduced.

#### Before we wrap up --
We should look at how we can use [`Pipeline`](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html) to 'merge' the two steps (PCA then LR) into a single object (see [example](https://scikit-learn.org/0.18/auto_examples/plot_digits_pipe.html) from docs).


```python
from sklearn.pipeline import Pipeline

pipe = Pipeline([
    ('reduce_dim', PCA()),
    ('predict', LinearRegression())
])
```


```python
pipe_scores = cross_val_score(pipe, scaled_feature_matrix, labels, scoring='neg_mean_squared_error', cv=25)
print(pipe_scores)
print(np.sqrt(-(pipe_scores).mean()))
```

    [-2029.08213624 -2511.97595623 -3167.47488694 -3040.84848828
     -3005.32593931 -4297.32798146 -3185.38675717 -2608.26146759
     -3161.14906526 -1841.86292552 -3174.37910643 -4724.69669729
     -2778.89952845 -2621.0163063  -2670.90134249 -4442.3548637
     -3868.38656242 -2148.98902673 -3122.92226801 -1944.12047966
     -4416.20769852 -5221.94361385 -1758.25084412 -1587.01950037
     -1823.63268618]
    54.827882004879235


> In practice, we could then go on to use [`GridSearchCV`](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html) to find the optimal number of components to use (if we were dealing with a larger data set). 
- But, we'll end there.
