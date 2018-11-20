---
title: "Neural Networks with Keras"
date: 2018-11-22
layout: post
math: true
category: blog
comments: true
tag:
- supervised classification
- neural network
- Pima Indian database
- Keras
author: adam
description: A tutorial on Keras that doesn't use the MNIST database.
---

Adapted from numerous sources, including Jason Brownlee's [article](https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/).

### Topic Guide
- [Learning Objectives](#learning-objectives)
- [Installing Dependencies](#dependencies)
- [Load Data](#load)
- [Define/Instantiate Model](#def-model)
- [Fit Model](#fit-model)
- [Evaluate Model Fit](#eval-model)
- [Exercise](#exercise)
- [Summary](#topic-review)


<a id="learning-objectives"></a>
## Learning Objectives
- Learn to define/instantiate neural network in Keras.
- See how to compile a Keras model using the efficient numerical backend.
- Understand how to train a model on data.
- See how/why evaluating a model's fit on data is so important.

---
<a id="dependencies"></a>
## Installing Dependencies
While the following example is relatively simple, it while depend on a few additional libraries that probably will not be present if you haven't installed them. These include:
- SciPy (including NumPy)
- Keras\*
    - As well as a Keras backend (Theano, TensorFlow, etc.)
>\* For installation: `$ pip install keras` 
>  For [more info](https://keras.io/#installation).

From the [Keras docs](https://keras.io/):
> "Keras is a *high-level* neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano. It was developed with a focus on enabling ***fast experimentation***."

This tutorial is intended to serve as a *brief*\* introduction to Keras, through an example similar to the types pipelines you've probably already seen. As such it can be broken down into these familiar steps:

- [Load Data](#load)
- [Define/Instantiate Model](#def-model)
- [Fit Model](#fit-model)
- [Evaluate Model Fit](#eval-model)

\*There will be relatively little code, as we'll move through the materials pretty slowly in order to emphasize clarity.

---
<a id="load"></a>
## Part 1. Load Data
Anytime you're working with stochastic processes, it's a good idea to see a random number seed for reproducibility of your results. Having added variation due to these processes can make optimization that much more laborious and difficult.


```python
# Import toolkits
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import pandas as pd
from sklearn import model_selection

# Fix random seed for reproducibility
np.random.seed(7)
```

This dataset comes from the UCI Machine Learning repository (see data dictionary [here](https://github.com/meccaLeccaHi/meccaLeccaHi.github.io/raw/master/assets/code/pima-indians-diabetes.txt)).

It was collected from the medical records of female Pima Indians (21 and older) and indicates whether they were diagnosed as diabetic within five years of collection. 

For this notebook, we'll use several different medical predictors as our independent variables and one outcome as our dependent variable: the onset of diabetes. Possible independent variables will include the number of pregnancies, BMI, insulin level, age, etc. *It will be necessary to follow the link to the data dictionary above for the complete description.*


```python
pima_data = pd.read_csv('../datasets/pima-indians-diabetes.csv', header=None)

# Count observations
print('Number of observations: {}'.format(pima_data.shape[0]))
# Count features
print('Number of features: {}'.format(pima_data.shape[1]-1))
```

    Number of observations: 768
    Number of features: 8


**Let's explore the data a bit before training...**

As we can see, this dataset contains eight input variables and one output variable (the last column), corresponding to 768 observations (patients) total. Once loaded we can split the dataset into input variables (X) and the output class variable (Y).

Our label, onset of diabetes as 1 or not as 0, implies that this is a *binary classification problem*.

These are all already in numeric format, which makes it easy to use directly with neural networks that expect numerical input and output values.


```python
# Split into input (X) and output (Y) variables
X = pima_data.iloc[:,0:6]
y = pima_data.iloc[:,8] # Onset of diabetes (True/False)

feature_num = X.shape[1]
```

As we've seen countless times by now, we always want to **split our data** into *training* and *testing* groups in order to be reasonably confident in our model's performance with new data.


```python
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, random_state=7)
```

---
<a id="def-model"></a>
## Part 2. Define/Instantiate Model

Models in Keras are defined as a sequence of layers.

When we create a `Sequential` model, we add layers one at a time until our network is complete.

One key thing is to ensure the input layer is expecting the right number of inputs. This can be specified when creating the first layer via the `input_dim` argument (e.g. `8` for 8 input variables).


```python
# Create model
model = Sequential() # Instantiate model ('Sequential' = A linear stack of layers)
model.add(Dense(12, input_dim=feature_num, activation='relu')) # 'Dense' = Fully-connected layer)
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
```

>For the purposed of today's class, we will skip over the role of optimizers, but activation functions, metric functions, and loss functions should be pretty familiar concepts by now. You are encouraged to research each of these concepts as part of the exercise later in this notebook.

Notice that we are using the rectifier (‘relu‘) activation function on the first two layers and the sigmoid function in the output layer. We've learned about the sigmoid function, and indeed, it used to be the case that sigmoid activation functions were preferred for all layers. More recently (~2011), however, better performance has been found with the [rectifier activation function](https://en.wikipedia.org/wiki/Rectifier_(neural_networks)), which has become the most popular activation function for deep neural networks. We still use a sigmoid on the output layer to ensure our network output is between 0 and 1 and maps easily to a probability of class 1.

Determining the best shape for your model can involve quite a bit of trial and error. But, in general, your network needs to be large enough to represent the complexity of the problem at hand, and ideally not larger than that (for speed's sake).

#### Compile the model
Now that the model is defined, it must be compiled.

Compiling uses the 'back-end' (i.e. the efficient numerical libraries under the covers, such as Theano or TensorFlow), to automatically choose the best way representation of this operation given your specific hardware, such as CPU, GPU, or distributed.


```python
# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
```

#### Visualize the model
It can be useful to routinely visualize our model, if only for QA purposes. Keras has a built-in method that works pretty well, but requires that Pydot be installed\* to do so.

*To install: `$pip install pydot` and `$brew install graphviz` (for mac)

In our current example (below), we can see that we're using a fully-connected network structure consisting of with three layers.

{% include figure.html url="/assets/images/keras_tutorial/model.png" caption="Fully-connected model schematic." width="40%" %}

We can specify the number of neurons in each layer, as well as the activation function, in the process of creating our model.


```python
from keras.utils import plot_model
plot_model(model, to_file='model.png', show_shapes=True)
```

The first layer has 12 neurons and expects $N_{features}$ input variables. The second hidden layer has 8 neurons and finally, the output layer has 1 neuron to make our binary categorical prediction (onset of diabetes or not).

---
<a id="fit-model"></a>
## Part 3. Fit Model

We can train or fit our model on our loaded data by calling the `fit()` function on the model.

The training process will run for a fixed number of iterations through the dataset called `epochs`, that we must specify using the `nepochs` argument. We can also set the number of instances that are evaluated before a weight update in the network is performed, called the batch size and set using the `batch_size` argument.

For this problem, we will run for a small number of iterations (150) and use a relatively small batch size of 10. Again, these are often selected experimentally by trial and error.

This is where most of the 'work' happens.


```python
# Fit the model
model.fit(X_train, y_train, epochs=150, batch_size=10)
```

    Epoch 1/150
    576/576 [==============================] - 0s 720us/step - loss: 4.2283 - acc: 0.6181
    Epoch 2/150
    576/576 [==============================] - 0s 181us/step - loss: 2.6341 - acc: 0.5868
    Epoch 3/150
    576/576 [==============================] - 0s 165us/step - loss: 0.8497 - acc: 0.6094
    Epoch 4/150
    576/576 [==============================] - 0s 224us/step - loss: 0.7465 - acc: 0.6181 0s - loss: 0.7597 - acc: 0.602
    Epoch 5/150
    576/576 [==============================] - 0s 278us/step - loss: 0.7375 - acc: 0.5816
    Epoch 6/150
    576/576 [==============================] - 0s 147us/step - loss: 0.6886 - acc: 0.6094
    Epoch 7/150
    576/576 [==============================] - 0s 138us/step - loss: 0.6722 - acc: 0.6354
    Epoch 8/150
    576/576 [==============================] - 0s 136us/step - loss: 0.6689 - acc: 0.6406
    Epoch 9/150
    576/576 [==============================] - 0s 136us/step - loss: 0.6523 - acc: 0.6476
    Epoch 10/150
    576/576 [==============================] - 0s 137us/step - loss: 0.6409 - acc: 0.6354
    Epoch 11/150
    576/576 [==============================] - 0s 136us/step - loss: 0.6647 - acc: 0.6215
    Epoch 12/150
    576/576 [==============================] - 0s 223us/step - loss: 0.6268 - acc: 0.6563
    Epoch 13/150
    576/576 [==============================] - 0s 192us/step - loss: 0.6174 - acc: 0.6684
    Epoch 14/150
    576/576 [==============================] - 0s 178us/step - loss: 0.6128 - acc: 0.6927
    Epoch 15/150
    576/576 [==============================] - 0s 161us/step - loss: 0.5969 - acc: 0.6979
    Epoch 16/150
    576/576 [==============================] - 0s 196us/step - loss: 0.6083 - acc: 0.6736
    Epoch 17/150
    576/576 [==============================] - 0s 247us/step - loss: 0.5980 - acc: 0.6840
    Epoch 18/150
    576/576 [==============================] - 0s 212us/step - loss: 0.5892 - acc: 0.6840
    Epoch 19/150
    576/576 [==============================] - 0s 171us/step - loss: 0.5943 - acc: 0.6944
    Epoch 20/150
    576/576 [==============================] - 0s 173us/step - loss: 0.5835 - acc: 0.7083
    Epoch 21/150
    576/576 [==============================] - 0s 235us/step - loss: 0.5879 - acc: 0.7031
    Epoch 22/150
    576/576 [==============================] - 0s 246us/step - loss: 0.5941 - acc: 0.6927
    Epoch 23/150
    576/576 [==============================] - 0s 199us/step - loss: 0.5844 - acc: 0.7135
    Epoch 24/150
    576/576 [==============================] - 0s 180us/step - loss: 0.6150 - acc: 0.6736
    Epoch 25/150
    576/576 [==============================] - 0s 225us/step - loss: 0.5932 - acc: 0.7014
    ...
    Epoch 125/150
    576/576 [==============================] - 0s 153us/step - loss: 0.5104 - acc: 0.7552
    Epoch 126/150
    576/576 [==============================] - 0s 171us/step - loss: 0.5125 - acc: 0.7309
    Epoch 127/150
    576/576 [==============================] - 0s 158us/step - loss: 0.5217 - acc: 0.7240
    Epoch 128/150
    576/576 [==============================] - 0s 160us/step - loss: 0.5048 - acc: 0.7309
    Epoch 129/150
    576/576 [==============================] - 0s 157us/step - loss: 0.5179 - acc: 0.7257
    Epoch 130/150
    576/576 [==============================] - 0s 159us/step - loss: 0.5164 - acc: 0.7413
    Epoch 131/150
    576/576 [==============================] - 0s 147us/step - loss: 0.5135 - acc: 0.7378
    Epoch 132/150
    576/576 [==============================] - 0s 151us/step - loss: 0.5139 - acc: 0.7361
    Epoch 133/150
    576/576 [==============================] - 0s 152us/step - loss: 0.5145 - acc: 0.7431
    Epoch 134/150
    576/576 [==============================] - 0s 154us/step - loss: 0.5133 - acc: 0.7378
    Epoch 135/150
    576/576 [==============================] - 0s 155us/step - loss: 0.5275 - acc: 0.7309
    Epoch 136/150
    576/576 [==============================] - 0s 146us/step - loss: 0.5135 - acc: 0.7378
    Epoch 137/150
    576/576 [==============================] - 0s 156us/step - loss: 0.5090 - acc: 0.7396
    Epoch 138/150
    576/576 [==============================] - 0s 148us/step - loss: 0.5234 - acc: 0.7344
    Epoch 139/150
    576/576 [==============================] - 0s 153us/step - loss: 0.5132 - acc: 0.7413
    Epoch 140/150
    576/576 [==============================] - 0s 169us/step - loss: 0.5116 - acc: 0.7309
    Epoch 141/150
    576/576 [==============================] - 0s 160us/step - loss: 0.5112 - acc: 0.7344
    Epoch 142/150
    576/576 [==============================] - 0s 176us/step - loss: 0.5155 - acc: 0.7309
    Epoch 143/150
    576/576 [==============================] - 0s 174us/step - loss: 0.5059 - acc: 0.7517
    Epoch 144/150
    576/576 [==============================] - 0s 165us/step - loss: 0.5068 - acc: 0.7431
    Epoch 145/150
    576/576 [==============================] - 0s 165us/step - loss: 0.5023 - acc: 0.7326
    Epoch 146/150
    576/576 [==============================] - 0s 164us/step - loss: 0.5212 - acc: 0.7378
    Epoch 147/150
    576/576 [==============================] - 0s 144us/step - loss: 0.5076 - acc: 0.7483
    Epoch 148/150
    576/576 [==============================] - 0s 157us/step - loss: 0.5121 - acc: 0.7309
    Epoch 149/150
    576/576 [==============================] - 0s 166us/step - loss: 0.5091 - acc: 0.7413
    Epoch 150/150
    576/576 [==============================] - 0s 149us/step - loss: 0.5006 - acc: 0.7517


    <keras.callbacks.History at 0x1a183d1748>

---
<a id="eval-model"></a>
## Part 4. Evaluate Model Fit


```python
# Evaluate the model
scores = model.evaluate(X_test, y_test)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
```

    192/192 [==============================] - 0s 302us/step
    
    acc: 71.88%


You can evaluate your model on your training dataset using the `evaluate()` function on your model and pass it the data used to evaluate the model's fit (i.e. 'testing data').

As we've seen before, `predict()` can be used to generate a prediction for each input.


```python
# Calculate predictions
predictions = model.predict(X).round().astype(int)

# Convert to more human-readable format
target_key = {1: 'Diabetic', 0: 'Not Diabetic'}
print(pd.Series(np.squeeze(predictions)).map(target_key).head())
```

    0        Diabetic
    1    Not Diabetic
    2    Not Diabetic
    3    Not Diabetic
    4        Diabetic
    dtype: object

---
<a id="exercise"></a>
## Part 5. Exercise

Now it's your turn. Update the code below to complete the following steps.

1. **Train-test split**
You probably already noticed one problem with our code- we're using the same data for training and testing (*oh no!*). Fix this. See what happens to our expectations regarding how the model will perform with future data.

2. **Feature selection**
We are only using a small number of the features available. Take a look at the data dictionary to understand the different variables contained in this dataset. Then, try changing which features are included based on your new understanding of the data. See if your score improves.

3. **Parameter tuning**
Optimization algorithms helps us to minimize (or maximize) loss (or reward) functions. Keras has a [variety](https://keras.io/optimizers/) of optimizers available for you to use. Take a look at a few that are available, try to find the right one for our model, and apply it.
Similarly, see if you can implement a different [metric function](https://keras.io/metrics/) or [loss function](https://keras.io/losses/).


```python
## Create your first MLP in Keras
# Fix random seed for reproducibility
np.random.seed(7)

# Split into input (X) and output (Y) variables
X = pima_data.iloc[:,0:1] 
y = pima_data.iloc[:,8] # Onset of diabetes (True/False)
feature_num = X.shape[1] # Number of features in our model

# Create model
model = Sequential()
model.add(Dense(12, input_dim=feature_num, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile model
model.compile(loss='mean_absolute_error', optimizer='sgd', metrics=['accuracy'])

# Fit the model
model.fit(X, y, epochs=50, batch_size=10, verbose=1)

# Evaluate the model
scores = model.evaluate(X, y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
```

    Epoch 1/50
    768/768 [==============================] - 0s 376us/step - loss: 0.4796 - acc: 0.6510
    Epoch 2/50
    768/768 [==============================] - 0s 97us/step - loss: 0.4613 - acc: 0.6510
    Epoch 3/50
    768/768 [==============================] - 0s 140us/step - loss: 0.4433 - acc: 0.6510
    Epoch 4/50
    768/768 [==============================] - 0s 128us/step - loss: 0.4268 - acc: 0.6510
    Epoch 5/50
    768/768 [==============================] - 0s 118us/step - loss: 0.4130 - acc: 0.6510
    Epoch 6/50
    768/768 [==============================] - 0s 112us/step - loss: 0.4021 - acc: 0.6510
    Epoch 7/50
    768/768 [==============================] - 0s 131us/step - loss: 0.3935 - acc: 0.6510
    Epoch 8/50
    768/768 [==============================] - 0s 111us/step - loss: 0.3868 - acc: 0.6510
    Epoch 9/50
    768/768 [==============================] - 0s 133us/step - loss: 0.3814 - acc: 0.6510
    Epoch 10/50
    768/768 [==============================] - 0s 133us/step - loss: 0.3771 - acc: 0.6510
    Epoch 11/50
    768/768 [==============================] - 0s 119us/step - loss: 0.3737 - acc: 0.6510
    Epoch 12/50
    768/768 [==============================] - 0s 110us/step - loss: 0.3708 - acc: 0.6510
    Epoch 13/50
    768/768 [==============================] - 0s 116us/step - loss: 0.3685 - acc: 0.6510
    Epoch 14/50
    768/768 [==============================] - 0s 131us/step - loss: 0.3665 - acc: 0.6510
    Epoch 15/50
    768/768 [==============================] - 0s 125us/step - loss: 0.3648 - acc: 0.6510
    Epoch 16/50
    768/768 [==============================] - 0s 123us/step - loss: 0.3634 - acc: 0.6510
    Epoch 17/50
    768/768 [==============================] - 0s 120us/step - loss: 0.3622 - acc: 0.6510
    Epoch 18/50
    768/768 [==============================] - 0s 127us/step - loss: 0.3611 - acc: 0.6510
    Epoch 19/50
    768/768 [==============================] - 0s 152us/step - loss: 0.3602 - acc: 0.6510
    Epoch 20/50
    768/768 [==============================] - 0s 129us/step - loss: 0.3594 - acc: 0.6510
    Epoch 21/50
    768/768 [==============================] - 0s 118us/step - loss: 0.3587 - acc: 0.6510
    Epoch 22/50
    768/768 [==============================] - 0s 139us/step - loss: 0.3580 - acc: 0.6510
    Epoch 23/50
    768/768 [==============================] - 0s 116us/step - loss: 0.3575 - acc: 0.6510
    Epoch 24/50
    768/768 [==============================] - 0s 131us/step - loss: 0.3569 - acc: 0.6510
    Epoch 25/50
    768/768 [==============================] - 0s 126us/step - loss: 0.3565 - acc: 0.6510
    Epoch 26/50
    768/768 [==============================] - 0s 111us/step - loss: 0.3561 - acc: 0.6510
    Epoch 27/50
    768/768 [==============================] - 0s 128us/step - loss: 0.3557 - acc: 0.6510
    Epoch 28/50
    768/768 [==============================] - 0s 134us/step - loss: 0.3553 - acc: 0.6510
    Epoch 29/50
    768/768 [==============================] - 0s 117us/step - loss: 0.3550 - acc: 0.6510
    Epoch 30/50
    768/768 [==============================] - 0s 118us/step - loss: 0.3547 - acc: 0.6510
    Epoch 31/50
    768/768 [==============================] - 0s 113us/step - loss: 0.3544 - acc: 0.6510
    Epoch 32/50
    768/768 [==============================] - 0s 140us/step - loss: 0.3542 - acc: 0.6510
    Epoch 33/50
    768/768 [==============================] - 0s 116us/step - loss: 0.3540 - acc: 0.6510
    Epoch 34/50
    768/768 [==============================] - 0s 118us/step - loss: 0.3537 - acc: 0.6510
    Epoch 35/50
    768/768 [==============================] - 0s 145us/step - loss: 0.3536 - acc: 0.6510
    Epoch 36/50
    768/768 [==============================] - 0s 124us/step - loss: 0.3534 - acc: 0.6510
    Epoch 37/50
    768/768 [==============================] - 0s 132us/step - loss: 0.3532 - acc: 0.6510
    Epoch 38/50
    768/768 [==============================] - 0s 145us/step - loss: 0.3530 - acc: 0.6510
    Epoch 39/50
    768/768 [==============================] - 0s 113us/step - loss: 0.3529 - acc: 0.6510
    Epoch 40/50
    768/768 [==============================] - 0s 114us/step - loss: 0.3527 - acc: 0.6510
    Epoch 41/50
    768/768 [==============================] - 0s 145us/step - loss: 0.3526 - acc: 0.6510
    Epoch 42/50
    768/768 [==============================] - 0s 133us/step - loss: 0.3525 - acc: 0.6510
    Epoch 43/50
    768/768 [==============================] - 0s 114us/step - loss: 0.3524 - acc: 0.6510
    Epoch 44/50
    768/768 [==============================] - 0s 118us/step - loss: 0.3522 - acc: 0.6510
    Epoch 45/50
    768/768 [==============================] - 0s 140us/step - loss: 0.3521 - acc: 0.6510
    Epoch 46/50
    768/768 [==============================] - 0s 121us/step - loss: 0.3520 - acc: 0.6510
    Epoch 47/50
    768/768 [==============================] - 0s 120us/step - loss: 0.3519 - acc: 0.6510
    Epoch 48/50
    768/768 [==============================] - 0s 106us/step - loss: 0.3519 - acc: 0.6510
    Epoch 49/50
    768/768 [==============================] - 0s 132us/step - loss: 0.3518 - acc: 0.6510
    Epoch 50/50
    768/768 [==============================] - 0s 121us/step - loss: 0.3517 - acc: 0.6510
    768/768 [==============================] - 0s 79us/step
    
    acc: 65.10%

---
<a id="topic-review"></a>
## Summary

Specifically, you saw all of the five essential steps  tocreate a neural network or deep learning model using Keras, including:

- How to define/instantiate neural network in Keras.
- How to compile a Keras model using the efficient numerical backend.
- How to train a model on data.
- How to evaluate a model's fit on data.

**Questions?** Leave a comment below.
