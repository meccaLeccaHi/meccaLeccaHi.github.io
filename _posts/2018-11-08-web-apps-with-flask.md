---
title: "Web apps with Flask"
date: 2018-11-08
layout: post
math: false
category: blog
comments: true
tag:
- Virtual environments
- Environmental variables
- Flask
- Googlemaps
- SQL
- HTML/CSS
author: adam
description: Post on using Flask (Postgres, Heroku, etc.) to make a super simple web app
---

# <img src="https://raw.githubusercontent.com/meccaLeccaHi/snowblog/master/app/static/images/yeti.gif" alt="Yeti from SkiFree on Windows 95" width="7%" height="auto">Snowblog!
> If you've ever found yourself wondering what a snowblog is, why on earth some one would want one, or maybe just how to get started with Flask, this post may be for *you*!

When Jerry isn't [dodging yeti's](https://ski.ihoc.net/), he loves tearing up the slopes! This is a simple app that allows Jerry to keep track of his experiences at different ski resorts, and find new ones based on his location! This is a beginner-friendly example of a simple [Flask](http://flask.pocoo.org/) application, that uses [Bootstrap](http://getbootstrap.com) as the CSS framework and [SQLite](https://www.sqlite.org/) as the database. It's designed to help demonstrate the use of Flask, within the context of an introductory Python course. As such, the code in this repo is deliberately simplified and heavily-commented for clarity.

### View online at:
[https://snowblogg.herokuapp.com/index](https://snowblogg.herokuapp.com/index)
### View the code at:
[https://github.com/meccaLeccaHi/snowblog](https://github.com/meccaLeccaHi/snowblog)

>This project was inspired by numerous sources, most notably: 
>- [*New and Improved Flask Mega-Tutorial*](http://neuralnetworksanddeeplearning.com/chap1.html) by *Miguel Grinberg* (Highly recommended)

>Dependencies: Numpy, Scipy, [Flask](http://flask.pocoo.org/), and [Googlemaps](https://github.com/googlemaps/google-maps-services-python).
>
>To run, execute the following commands:
```
$ sudo apt-get -y install python3 python3-venv python3-dev  
$ git clone https://github.com/meccaLeccaHi/snowblog  
$ cd snowblog  
$ python3 -m venv venv  
$ source venv/bin/activate  
(venv)$ export FLASK_APP=microblog.py  
(venv)$ export GOOGLE_KEY='API_KEY_HERE'  
(venv)$ pip install flask-bootstrap flask-migrate flask-sqlalchemy flask-wtf numpy scipy googlemaps  
(venv)$ flask run
```

This project served as a nice opportunity to get more familiar with Flask, with the intent of eventually building an app of greater utility down the road (perhaps integrating [Plotly](https://plot.ly/products/dash/)). For now let's learning about the essential components involved with Flask. But first, a brief primer on virtual environments and environmental variables.

## Setting up the environment

Obviously, we are going to use Python 3 in this post as we have for all the others. So, if it's not installed, we can change that like so:  
`$ sudo apt-get -y install python3 python3-venv python3-dev`

### Virtual environments
A _virtual environment_ is an enclosed copy of the Python interpreter. By that I mean that when you install Python packages in a virtual environment (as opposed to the system-wide Python interpreter), only the virtual environment is affected. This provides us greater freedom to experiment with numerous environments in parallel, while keeping the changes in each separate from the others.
- This also allows others to re-create your environment more easily, as we'll see below.
- Plus, they are 'owned' by the user who creates them, so they don't require a separate admin account.

#### Create environment
We can start by creating a virtual environment inside the project we are working on. So, from within that directory, run:  
>`$ python -m venv venv`\*  
>\*If we want to use a different interpreter (e.g. `python3` or `python2`), use that instead.

This command asks Python to run the `venv` package, and creates a virtual environment named `venv` (feel free to change it as you wish). 

Did you notice that a folder named `/venv` has now been created inside your project folder? 
Now that the environmet has been created, we install it like so:
>`$ virtualenv venv`


#### Activate environment
Having done so, we can `cd` into this package and 'activate' the appropriate virtual environment whenever we want like so:
>`$ source venv/bin/activate`   

Notice that the cursor will change from `$` to `(venv) $`

#### Install environment
Now, we're ready to start customizing our environment!
**Just remember**, the changes you make inside your virtual environment are unique to that environment, and will not exist if the environment is deactivated. The changes you make *are* persistent, however, and will stay the way they are left on the last time they are used.

#### Bonus: Enumerating packages with 'requirements.txt'
When installing software, and Python packages in particular, it's not un-common to end up with a lot of libraries installed.
We can get a quick, comprehensive list of what packages we are using at any time with the commands below:  
`$ pip freeze > requirements.txt`  

This directs the output of `pip freeze`, which lists all of the current Python package dependencies, to a text file named 'requirements.txt'. Open it up and take a look. 
The beauty of it is that it allows someone else to immediately adopt the same environment by running:  
>`$ pip install -r requirements.txt`


## Setting environmental variables
'Environmental variables' are one way for a particular environment to keep track of certain settings, and to pass thos settings between different processes within the same environment. They are usually employed to keep track of ephemeral data, such as location of the current working directory.

By convention, environmental variables are typically defined using all capital letters, which helps users distinguish environmental variables from other variable types.

As with most variables, variable assignment consists of relating a key to a value, in most instances a string, using the following format:  
`KEY="value with spaces"`

For example:
```
$ BASH=bin/bash
$ echo $BASH
bin/bash
```

#### Creating environmental variables
The variable `BASH` now exists within this current  environment, but will be destroyed as soon as this instance of the shell interpreter is closed. To make these variables persist, we use `export`, like so:  
`export BASH`
Our program will use two environmental variables. `FLASK_APP` and `GOOGLE_KEY`.
- `FLASK_APP` tells Flask how to import our application:  
`(venv) $ export FLASK_APP=microblog.py`
- `GOOGLE_KEY` provides the necessary API key for [googlemaps](https://github.com/googlemaps/google-maps-services-python)  
`(venv)$ export GOOGLE_KEY='API_KEY_HERE'`

One last thing to mention is that we can, if we desire, include the creation of these variables during login by adding the `export` commands to our `~/.bashrc` file (at the bottom is fine).


## Templates
Templates, as employed by Flask, are loosely analagous to a Python function, in that they are reusable sets of operations that accept pre-defined inputs and transform those inputs to produce a pre-defined output. In this case the inputs are the data required by different components of a webpage, and the output is the HTML webpage.  
This allows us to separate the 'back-end' data generation elements that determine the page's functionality, from the 'front-end' layout and presentation elements that determine the page's appearance.
In Flask, templates are stored as separate files inside a */templates* folder inside the application package. An example is shown in `index.html` below.  

<figcaption>index.html</figcaption>  
```
<html>
	<head>
		<title>Welcome to Snowblog</title>
	</head>
	<body>
		<h1>{{ "{{ user " }}}}'s snowblog</h1>
	</body>
</html>
```

This is a super simple HTML page that defines the title and a heading. But, notice the place holder for user's name in the heading? That's the adaptive component defined by whatever input is provided to the template. So when I the following:
`render_template('index.html', user='Jerry')`
 an HTML page is *rendered* like so:  
{% include figure.html url="/assets/images/flask_app/render_example.png" caption="Super simple HTML page produced from our `index.html` template." width="45%" %}

#### Template inheritance
An just like a Python function can contain other functions, templates can contain other templates. That way we can use them when we need to render commonly-occuring elements in our website, like the navigation bar or log-in page.
For example, if we define a base template and name it `base.html`, we could include a very simple navigation bar on every page that allows us to quickly navigate our entire site. So we can modify `index.html` to create `base.html` like so:

```
<html>
	<head>
		<title>Welcome to Snowblog</title>
	</head>
	<body>
		<div>Microblog: <a href="/index">Home</a></div>
		<hr>
		{{ "{% block content " }}%}{{ "{% endblock " }}%}
	</body>
</html>
```
<figcaption>base.html</figcaption>  

The `block` content above is how we reference other templates in jinja templates, such as these.
Now, `base.html` can save me from repeatedly adding (and maintaining) a navigation bar for each page of my website. Each page will inherit the same nav bar, while the `block` control statement above still allows me to insert the unique components of each page. For example, we can now simply set `index.html` to inherit the nav bar from `base.html` like so:  
<figcaption>`index.html` with inheritance from base template.</figcaption>  
```
{{ "{% extends 'base.html' " }}%}
{{ "{% block content " }}%}
	<h1>{% raw %}{{ user }}{% endraw %}'s snowblog</h1>
{{ "{% endblock " }}%}
```
{% include figure.html url="/assets/images/flask_app/block_example.png" caption="Rendering using template inheritance." width="45%" %}
From here on, whenever I need to create a new page for my website, I can simply derive them using `base.html` as a template, with the added bonus of having a more consistent, well-behaved application.

## Forms
So far, we've created a super simple template to provide the home page of our awesome new application. To start making this web site functional, we need to include mechanisms for users to input information using a variety of 'web forms'. *Web forms* are pages that users request using their browser. Upon these requests, the server uses HTML and other markup code to render the form in the client's browser. These forms then serve as the re-usable components that can be adapted to the particular needs of each application, without having to worry about the presentation.
Fortunately, Flask has an extension to handle web forms: [Flask-WTF](http://packages.python.org/Flask-WTF). We'll see more Flask extensions later on, since extensions are a central element in the Flask ecosystem.
> Like other Python packages, we can install Flask-WTF with `pip`.
```
(venv) $ pip install flask-wtf
```

### Locate Ski Resorts Form

For our first form, let's create the form we will use to locate ski resorts closest to the user based their location, which will have to be provided as text input.  Flask-WTF uses Python classes to represent each type of web form. So, in order to create a new form we define it as a new class whose variables represent the fields of the form. We can group our forms together in a new module *app/form.py* (see below).  
<figcaption>`app/form.py` with LocateForm class.</figcaption>  
```
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# Define class for location form
class LocateForm(FlaskForm):
	# Create address field
	address = StringField('Enter Address Below', validators=[DataRequired()])
	# Create submission button
	submit = SubmitField('Submit')
```
As you can see, we are importing a class from the WTForms package for each field type in the form. In this example, we create class variables for the string field and submit button within the `LocateForm` class. We also provide each field with a brief description, which can serve as a label later on.
The `validators` you noticed in the string field just assigns certain validation routines to the submission of data through these fields. In this case, `DataRequired` will just check and make sure the text field is not empty upon submission. But more complicated validators are also available.

### Form Templates
Now we just need to connect the form to an HTML template to render it in a browser. But Flask makes this simple by handling most of the HTML rendering for you. For example, the template for the location form is shown below.

<figcaption>`app/templates/locate.html` Location form template.</figcaption>  
```
{{ "{% extends 'base.html' " }}%}

{{ "{% block content " }}%}
	<h1>Locate ski resorts</h1>
	<form action="" method="post" novalidate>
		{{ "{{ form.hidden_tag() " }}}}
		<p>
			<b>{{ "{{ form.address.label " }}}}</b><br>
			{{ "{{ form.address(size=32) " }}}}<br>
			{{ "{% for error in form.address.errors " }}%}
			<span style="color: red;">{{ error }}</span>
			{{ "{% endfor " }}%}
		</p>
		<p>{{ "{{ form.submit() " }}}}</p>
	</form>
{{ "{% endblock " }}%}
```
As with `index.html`, this template is another extension of the `base.html` template that we've discussed already. This consistency is among the greatest advantages afforded by templates in Flask.

We can infer that this template expects a `form` argument upon instantiation. We'll see how that's handled below, in the last document that's required to implement our brilliant location form.

### Adding Location View
Now, let's add a new function to our `routes` module that defines the new `/locate` view that we've added to our website.  We do that by adding another function to *app/form.py* (see below). This is where we import and instantiate LocateForm from `forms.py`, while passing it to the template to be rendered.  

<figcaption>`app/routes.py` Adding `/locate` view.</figcaption>  
```
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LocateForm

# ...

# 'Locate ski resorts' view
@app.route('/locate', methods=['GET', 'POST'])
def locate():
	form = LocateForm()
	if form.validate_on_submit():
		
		# Provide user feedback
		flash('Finding ski resorts closest to: {}'.format(form.address.data))
		return redirect('/index')

	# Render webpage
	return render_template('locate.html', title="Find resorts", form=form)
```

**Optionally**, we might want to add the new 'locate' view to our navigation bar:

<span style="color: grey;">`app/templates/base.html` Updating navigation bar</span>


<figcaption>File: folderName/fileName.rb</figcaption>
```
<div>
	Snowblog:
	<a href="/index">Home</a>
	<a href="/locate">Locate</a>
</div>
```

And *viola*! Pretty neat, eh?

{% include figure.html url="/assets/images/flask_app/added_locate_view.png" caption="Added 'location' view to website." width="45%" %}

## Databases


