---
title: "Virtual Environments with Python"
date: 2019-02-12
layout: post
math: false
category: blog
comments: true
tag:
- Virtual environments
author: adam
description: A brief primer on setting up a 'standard' virtual environment on linux/unix systems
---

## Topic Guide
- [Learning Objectives](#learning-objectives)
- [Installing Dependencies](#dependencies)
- [Setting Up Virtual Environments](#virtual_environment)

<a id="learning-objectives"></a>
## Learning Objectives
- Understand how to use virtual environments in Python.

The following is a brief primer on setting up a 'standard' virtual environment on Linux/UNIX systems.

<a id="dependencies"></a>
## Installing Dependencies
Obviously, we are going to use Python 3 in this post as we have for all the others. So, if it's not installed, we can change that like so:
```
$ sudo apt-get -y install python3 python3-venv python3-dev
```

<a id="virtual_environment"></a>
### Virtual Environments
A _virtual environment_ is an enclosed copy of the Python interpreter. By that I mean that when you install Python packages in a virtual environment (as opposed to the system-wide Python interpreter), only the virtual environment is affected. This provides us greater freedom to experiment with numerous environments in parallel, while keeping the changes in each separate from the others.
- This also allows others to re-create your environment more easily, as we'll see below.
- Plus, they are 'owned' by the user who creates them, so they don't require a separate admin account.

#### Create the environment
>Note: The `conda` command is the preferred interface for managing installations and virtual environments with the Anaconda Python distribution. As such, if you are using Conda, then you may prefer to use the `conda` command to manage your virtual environments, instead of `virtualenv`. See [here](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/) for more info.

We can start by creating a virtual environment inside the project we are working on. So, from within that directory, run:
```
$ python -m venv venv
```
>Note: If we want to use a different interpreter (e.g. `python3` or `python2`), use that instead.

This command asks Python to run the `venv` package, and creates a virtual environment named `venv` (feel free to change it as you wish).

Did you notice that a folder named `/venv` has now been created inside your project folder?
Now that the environmet has been created, we install it like so:
```
$ virtualenv venv
```

#### Activating environments
Having done so, we can `cd` into this package and 'activate' the appropriate virtual environment whenever we want like so:
```
$ source venv/bin/activate
```

Notice that the cursor will change from `$` to `(venv) $`

#### Install the environment
Now, we're ready to start customizing our environment!
**Just remember**, the changes you make inside your virtual environment are unique to that environment, and will not exist if the environment is deactivated. The changes you make *are* persistent, however, and will stay the way they are left on the last time they are used.

#### Bonus: Enumerating packages with 'requirements.txt'
When installing software, and Python packages in particular, it's not un-common to end up with a lot of libraries installed.
We can get a quick, comprehensive list of what packages we are using at any time with the commands below:
```
$ pip freeze > requirements.txt
```

This directs the output of `pip freeze`, which lists all of the current Python package dependencies, to a text file named 'requirements.txt'. Open it up and take a look.
The beauty of it is that it allows someone else to immediately adopt the same environment by running:
```
$ pip install -r requirements.txt
```

**Questions?** Leave a comment below.
