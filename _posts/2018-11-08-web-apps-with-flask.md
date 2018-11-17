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
>
>This project was inspired by numerous sources, most notably: 
>- [*New and Improved Flask Mega-Tutorial*](http://neuralnetworksanddeeplearning.com/chap1.html) by *Miguel Grinberg* (Highly recommended)

When Jerry isn't [dodging yeti's](https://ski.ihoc.net/), he loves tearing up the slopes! This is a simple app that allows Jerry to keep track of his experiences at different ski resorts, and find new ones based on his location! This is a beginner-friendly example of a simple [Flask](http://flask.pocoo.org/) application, that uses [Bootstrap](http://getbootstrap.com) as the CSS framework and [SQLite](https://www.sqlite.org/) as the database. It's designed to help demonstrate the use of Flask, within the context of an introductory Python course. As such, the code in this post is deliberately simplified and heavily-commented for clarity.

## Topic Guide
- [Learning Objectives](#learning-objectives)
- [Installing Dependencies](#dependencies)
- [Setting Up The environment](#environment)
    - [Virtual Environments](#virtual_environment)
    - [Setting Environmental Variables](#environmental_variables)
- [Templates](#templates)
    - [Template Inheritance](#template_inheritance)
- [Forms](#forms)
    - [Locate Resorts Form](#locate_form)
    - [Form Templates](#form_templates)
    - [Add Location View](#add_view)
    - [Using Data From Forms](#form_data)
- [Databases](#databases)
    - [Database Models](#database_models)

- [HTML/CSS](#html_css)
- [Topic Review](#topic-review)


<a id="learning-objectives"></a>
## Learning Objectives
- Understand how to use virtual environments in Python.
- Understand how to set environment variables in shell.
- Observe the utility of Flask as a powerful option for providing microservices via Python.
- Explore templates, forms, and other essential elements of the Flask ecosystem through a simple example.


### Try this app now at:
[https://snowblogg.herokuapp.com/index](https://snowblogg.herokuapp.com/index)
### View the code at:
[https://github.com/meccaLeccaHi/snowblog](https://github.com/meccaLeccaHi/snowblog)


<a id="dependencies"></a>
## Installing Dependencies
- Numpy
- Scipy
- [Flask](http://flask.pocoo.org/)
- [Googlemaps](https://github.com/googlemaps/google-maps-services-python).
>To get started, execute the following commands:
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

<a id="environment"></a>
## Setting Up The Environment

Obviously, we are going to use Python 3 in this post as we have for all the others. So, if it's not installed, we can change that like so:  
`$ sudo apt-get -y install python3 python3-venv python3-dev`

<a id="virtual_environment"></a>
### Virtual Environments
A _virtual environment_ is an enclosed copy of the Python interpreter. By that I mean that when you install Python packages in a virtual environment (as opposed to the system-wide Python interpreter), only the virtual environment is affected. This provides us greater freedom to experiment with numerous environments in parallel, while keeping the changes in each separate from the others.
- This also allows others to re-create your environment more easily, as we'll see below.
- Plus, they are 'owned' by the user who creates them, so they don't require a separate admin account.

#### Create the environment
We can start by creating a virtual environment inside the project we are working on. So, from within that directory, run:  
>`$ python -m venv venv`\*  
>\*If we want to use a different interpreter (e.g. `python3` or `python2`), use that instead.

This command asks Python to run the `venv` package, and creates a virtual environment named `venv` (feel free to change it as you wish). 

Did you notice that a folder named `/venv` has now been created inside your project folder? 
Now that the environmet has been created, we install it like so:
>`$ virtualenv venv`


#### Activating environments
Having done so, we can `cd` into this package and 'activate' the appropriate virtual environment whenever we want like so:
>`$ source venv/bin/activate`   

Notice that the cursor will change from `$` to `(venv) $`

#### Install the environment
Now, we're ready to start customizing our environment!
**Just remember**, the changes you make inside your virtual environment are unique to that environment, and will not exist if the environment is deactivated. The changes you make *are* persistent, however, and will stay the way they are left on the last time they are used.

#### Bonus: Enumerating packages with 'requirements.txt'
When installing software, and Python packages in particular, it's not un-common to end up with a lot of libraries installed.
We can get a quick, comprehensive list of what packages we are using at any time with the commands below:  
`$ pip freeze > requirements.txt`  

This directs the output of `pip freeze`, which lists all of the current Python package dependencies, to a text file named 'requirements.txt'. Open it up and take a look. 
The beauty of it is that it allows someone else to immediately adopt the same environment by running:  
>`$ pip install -r requirements.txt`

<a id="environmental_environment"></a>
### Setting Environmental Variables
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

<a id="templates"></a>
## Templates
Templates, as employed by Flask, are loosely analagous to a Python function, in that they are reusable sets of operations that accept pre-defined inputs and transform those inputs to produce a pre-defined output. In this case the inputs are the data required by different components of a webpage, and the output is the HTML webpage.  
This allows us to separate the 'back-end' data generation elements that determine the page's functionality, from the 'front-end' layout and presentation elements that determine the page's appearance.
In Flask, templates are stored as separate files inside a */templates* folder inside the application package. An example is shown in `index.html` below.  

<figcaption><i>app/templates/index.html</i><br>&nbsp;</figcaption>  
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
{% include figure.html url="/assets/images/flask/render_example.png" caption="Super simple HTML page produced from our `index.html` template." width="55%" %}

<a id="template_inheritance"></a>
### Template Inheritance
An just like a Python function can contain other functions, templates can contain other templates. That way we can use them when we need to render commonly-occuring elements in our website, like the navigation bar or log-in page.
For example, if we define a base template and name it `base.html`, we could include a very simple navigation bar on every page that allows us to quickly navigate our entire site. So we can modify `index.html` to create `base.html` like so:

<figcaption><i>app/templates/base.html</i><br>&nbsp;</figcaption>  
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

The `block` content above is how we reference other templates in jinja templates, such as these.
Now, `base.html` can save me from repeatedly adding (and maintaining) a navigation bar for each page of my website. Each page will inherit the same nav bar, while the `block` control statement above still allows me to insert the unique components of each page. For example, we can now simply set `index.html` to inherit the nav bar from `base.html` like so:  

<figcaption><i>app/templates/index.html</i> - Inheritance from base template.<br>&nbsp;</figcaption>  
```
{{ "{% extends 'base.html' " }}%}
{{ "{% block content " }}%}
	<h1>{{ "{{ user " }}}}'s snowblog</h1>
{{ "{% endblock " }}%}
```
{% include figure.html url="/assets/images/flask/block_example.png" caption="Rendering using template inheritance." width="55%" %}
From here on, whenever I need to create a new page for my website, I can simply derive them using `base.html` as a template, with the added bonus of having a more consistent, well-behaved application.

<a id="forms"></a>
## Forms
So far, we've created a super simple template to provide the home page of our awesome new application. To start making this web site functional, we need to include mechanisms for users to input information using a variety of 'web forms'. *Web forms* are pages that users request using their browser. Upon these requests, the server uses HTML and other markup code to render the form in the client's browser. These forms then serve as the re-usable components that can be adapted to the particular needs of each application, without having to worry about the presentation.
Fortunately, Flask has an extension to handle web forms: [Flask-WTF](http://packages.python.org/Flask-WTF). We'll see more Flask extensions later on, since extensions are a central element in the Flask ecosystem.
> Like other Python packages, we can install Flask-WTF with `pip`.
```
(venv) $ pip install flask-wtf
```
<a id="locate_form"></a>
### Locate Resorts Form

For our first form, let's create the form we will use to locate ski resorts closest to the user based their location, which will have to be provided as text input.  Flask-WTF uses Python classes to represent each type of web form. So, in order to create a new form we define it as a new class whose variables represent the fields of the form. We can group our forms together in a new module *app/form.py* (see below).  
<figcaption><i>app/form.py</i> - Now with LocateForm class.<br>&nbsp;</figcaption>  
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

<a id="form_templates"></a>
### Form Templates
Now we just need to connect the form to an HTML template to render it in a browser. But Flask makes this simple by handling most of the HTML rendering for you. For example, the template for the location form is shown below.

<figcaption><i>app/templates/locate.html</i> - Location form template.<br>&nbsp;</figcaption>  
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

<a id="add_view"></a>
### Add Location View
Now, let's add a new function to our `routes` module that defines the new `/locate` view that we've added to our website.  We do that by adding another function to *app/form.py* (see below). This is where we import and instantiate LocateForm from `forms.py`, while passing it to the template to be rendered.  

<figcaption><i>app/routes.py</i> - Adding location view.<br>&nbsp;</figcaption>  
```
from flask import render_template, redirect, url_for
from app import app
from app.forms import LocateForm

# ...

# 'Locate ski resorts' view
@app.route('/locate', methods=['GET', 'POST'])
def locate():
	form = LocateForm()

	# Render webpage
	return render_template('locate.html', title="Find resorts", form=form)
```

***Optionally***, we might want to add the new location view to our navigation bar:

<figcaption><i>app/templates/base.html</i> - Updating navigation bar.<br>&nbsp;</figcaption>
```
<div>
	Snowblog:
	<a href="/index">Home</a>
	<a href="/locate">Locate</a>
</div>
```

And *viola*! Pretty neat, eh?

{% include figure.html url="/assets/images/flask/added_locate_view.png" caption="Added 'location' view to website." width="55%" %}

<a id="form_data"></a>
### Using Data From Forms

While this may look nice, anyone who was brave enough to click on 'submit' would find that we get an error: "Method Not Allowed". That's simply because we still need to provide our web form with some logic telling it how to handle the data provided by the user. We accomplish that by modifying our definition of the `locate` class in `routes.py` (see below).

<figcaption><i>app/routes.py</i> - Adding user feedback.<br>&nbsp;</figcaption>  
```
from flask import render_template, flash, redirect, url_for
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
Now, when `form.validate_on_submit()` returns as `True`, the `locate` function executes two more functions, imported from Flask. `flash()` essentially records a message at the end of one request, then accesses it on the next request and only next request. `redirect()` is pretty self-explanatory; it tells the client's browser to navigate to a certain page (supplied as an argument).

To make this work, we just need to add some way of rendering those flashed messages in our existing templates. By adding that to base template (see below), all of our pages will inherit this functionality.

<figcaption><i>app/templates/base.html</i> - Adding flashed messages.<br>&nbsp;</figcaption>  
```
from flask import render_template, flash, redirect, url_for
# ...

# 'Locate ski resorts' view
<html>
    <head>
		<title>Welcome to Snowblog</title>
	</head>
    <body>
        <div>
            Snowblog:
            <a href="/index">Home</a>
            <a href="/locate">Locate</a>
        </div>
        <hr>
        {{ "{% with messages = get_flashed_messages() " }}%}
        {{ "{% if messages " }}%}
        <ul>
            {{ "{% for message in messages " }}%}
            <li>{{ "{{ message " }}}}</li>
            {{ "{% endfor " }}%}
        </ul>
        {{ "{% endif " }}%}
        {{ "{% endwith " }}%}
        {{ "{% block content " }}%}{{ "{% endblock " }}%}
    </body>
</html>
```
Here we are calling `get_flashed_messages` and assigning the output to `messages`, which we iteratively print to our page as items in a list (notice the `<ul>` and `<li>` elements). The convenient thing about flashed messsages is that they cease to exist after they have been displayed, so they will not appear again on subsequent page views. Their purpose is typically to convey errors or warnings to the user as they occur. Now, when we hit 'submit', we are redirected to the home page and given a feedback message about our input.

{% include figure.html url="/assets/images/flask/flashed_message_example.png" caption="Flashed message example." width="55%" %}

<a id="databases"></a>
## Databases

So far, we've covered a lot of ground, but have left out a major component that will be necessary for even the simplest of applications. Flask works with a variety of databases, including those that use SQL ('relational') and others that don't (i.e. *NoSQL*).

For this project, we'll use another Flask extension: [Flask-SQLAlchemy](http://packages.python.org/Flask-SQLAlchemy), which provides a wrapper to incorporate [SQLAlchemy](http://www.sqlalchemy.org) into the Flask ecosystem. [Object Relational Mappers](http://en.wikipedia.org/wiki/Object-relational_mapping) (ORM's) provide a way to handle databases of tables as if they were simply Python objects. This saves a lot of the effort of switching between the use of Python and SQL during administration of our site.

As we saw before, we can simply install the package in our virtual environment using `pip`.
```
(venv) $ pip install flask-sqlalchemy
```

For small, 'light-weight' applications such as these, SQLite is a convenient database options since it takes the form of file on the hard drive, rather than a server that needs to be connected to (e.g. PostgreSQL or MySQL). To make our dream a reality, we need to make some changes to our config file:

<figcaption><i>config.py</i> - Setting up Flask-SQLAlchemy.<br>&nbsp;</figcaption>  
```
import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Assign app configuration variables (or retrieve them from the os, if they exist there)
class Config(object):
    GOOGLE_KEY = os.environ.get('GOOGLE_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```
Now, we've added a few variables to our `Config` class, including `SQLALCHEMY_DATABASE_URI`, which tells Flask where to find database for our application. Since `DATABASE_URL` is requested from the shell, it must be set as an environmental variable for Flask to use it, otherwise it will fall back and use the other value that was provided.

Setting `SQLALCHEMY_TRACK_MODIFICATIONS` to false just avoids an unecessary, extra step every time a change is made to our database. 

We also need to make sure our database is instantiated. This will take place as part of the creation of our app in `app/__init__.py`:

<figcaption><i>app/__init__.py</i> - Adding databases.<br>&nbsp;</figcaption>  
```
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Create instances of app components to be included
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
```
We can use the same pattern for adding any Flask extension: we first initialize our Flask extension, then import `routes` and `models` modules. We've seen `routes` previously, and `models` is defined in the next section of this post.

<a id="database_models"></a>
## Database Models

In order for the ORM to properly translate between objects and databases, we need to define our 'database models'. Our goal is to create the following two tables. 

{% include figure_link.html url="/assets/images/flask/db_models.png" href="http://ondras.zarovi.cz/sql/demo" caption="Database tables (made with WWW SQL Designer)" width="55%" %}

In both tables, `id` serves as the 'primary key', while the rows in `Resort` refer to ski resorts and the rows in `Post` refer to posts about those resorts. As defined below, `resortname`, `state`, `url`, and `body` fields expect strings as their entries, whereas `id`, `latitude`, and `longitude` are purely numeric.


<figcaption><i>app/models.py</i> - Creating database models.<br>&nbsp;</figcaption>  
```
from app import db

# Define 'Resort' table
class Resort(db.Model):
	# Define table columns
	id = db.Column(db.Integer, primary_key=True)
	resortname = db.Column(db.String(64), index=True)
	state = db.Column(db.String(2))
	latitude = db.Column(db.Integer)
	longitude = db.Column(db.Integer)
	url = db.Column(db.String(128))

	# Define the representation of instances of this class
	def __repr__(self):
		return '<Resort {}>'.format(self.resortname)

# Define 'Post' table
class Post(db.Model):
	# Define table columns
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(256))
	resortname = db.Column(db.String(64), index=True)

	# Define the representation of instances of this class
	def __repr__(self):
		return '<Post {}>'.format(self.body)
```

Here we've defined two classes (`Resort` and `User`), which inherit from `db.Model`. The `__repr__` method returns a printable representation of the object, which can be helpful for de-bugging.

```
>>> from app.models import Resort
>>> r = Resort(resortname='Kentucky Snowbowl', state='KY', latitude=20, longitude=-20, url='www.kysnowbowl.com')
>>> r
<Resort Kentucky Snowbowl>
```

Now, we can create the migration repository for snowblog by running `flask db init`.
With that in place, we finally complete the first migration of our database to the new format. We can do so automatically, using the schema defined by our models, with the `flask db migrate` command. Notice that this command creates a migration script, and the location is provided upon running the `migrate` command (see below). Although we won't cover it here, you are free to manipulate the migration script yourself, as you see fit.

```
(venv) flask db migrate
INFO  [alembic.runtime.migration] Context impl SQLiteImpl.
INFO  [alembic.runtime.migration] Will assume non-transactional DDL.
INFO  [alembic.autogenerate.compare] Detected added table 'post'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_post_resortname' on '['resortname']'
INFO  [alembic.autogenerate.compare] Detected added table 'resort'
INFO  [alembic.autogenerate.compare] Detected added index 'ix_resort_resortname' on '['resortname']'
  Generating /home/Jerry/snowblog/migrations/versions/c544f524e5ed_.py ... done
```
With the migration script now ready, we can apply the changes to the database via `flask db upgrade`.

<a id="html_css"></a>
## HTML/CSS



From this point, it should be fairly easy to continue to modify the existing code to suite your specific needs. **Have fun!**

<a id="topic-review"></a>
## Topic Review
---
- We learned about the use of virtual environments in Python.
- We saw how environmental variables are set in the shell.
- We learned how to use templates and forms to quickly construct a 'lightweight' application that allows us to focus on website functionality and not on the presentation/HTML.
- We learned about the variety of database options available to use with Flask.
