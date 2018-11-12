---
title: "Web apps with Flask"
date: 2018-11-08
layout: post
math: false
category: blog
tag:
- Flask
- Googlemaps
- SQL databases
- HTML/CSS
author: adam
description: Post on using Flask (Postgres, Heroku, etc.) to make a super simple web app
---

# <img src="./app/static/images/yeti.gif" alt="Yeti from SkiFree on Windows 95" width="10%" height="auto">Snowblog!
> If you've ever found yourself wondering what a snowblog is, why on earth someone would want one, or how to get started with Flask, this post may be for *you*!

This is a simple app that allows Jerry to keep track of his experiences at different ski resorts, and find new ones based on his location input! This is a beginner-friendly example of a simple [Flask](http://flask.pocoo.org/) application, that uses [Bootstrap](http://getbootstrap.com) as the CSS framework and [SQLite](https://www.sqlite.org/) as the database. It's designed to help demonstrate the use of Flask, within the context of an introductory Python course. As such, the code in this repo is deliberately simplified and heavily-commented for clarity.

### View online at:
https://snowblogg.herokuapp.com/index
### View the code at:
https://github.com/meccaLeccaHi/snowblog

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

