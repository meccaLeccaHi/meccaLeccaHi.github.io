---
layout: page
title: Projects
category: project
---

<h1 class="title">{{ page.title }}</h1>

<section class="list">

</section>

> #### You can find most of my work on [GitHub](https://github.com/meccaLeccaHi). Several posts on my [blog](../blog/) are also related to these projects.

---

### Face-morphing -- ***Spring 2016*** -- [GH repo](https://github.com/meccaLeccaHi/face_morphing)
This was the first project that got me really hooked on the exciting possibilities in open-source programming.
Starting in grad school, I had been on the lookout for a method of morphing faces without the tedium of manually-placing hundreds of 'points' on each face.
Quite unexpectedly, I found that I was able to get really good results using image segmentation tools ([ANTs](http://stnava.github.io/ANTs/), namely), which had actually been designed application to MRI images of the brain. Here was a tool that excelled at unsupervised alignment of anatomical brain scans, and we were able to use it (quite successfully) to align (and transition between) different faces. This worked really well for morphing between stationary faces in an entirely 'unsupervised' fashion (see figure below).

{% include figure.html url="https://camo.githubusercontent.com/ef03ccb71de920c61fb5d4e96afdba923c91cb4c/687474703a2f2f692e696d6775722e636f6d2f3476683858784b2e706e67" caption="Face morphing via image segmentation and alignment." width="70%" %}

My main interest was in using 'life-like' clips of moving, talking faces, however. So soon after, I began a collaboration with [Supasorn Suwajanakorn](http://www.supasorn.com//), then at Washington University. He had created these really nice controllable models of a handful of different celebrities (link [here](http://grail.cs.washington.edu/projects/3DPersona/)). With them, we were prepared to apply the same segmentation technique to each frame of a short video.

Obviously, this required a substantial increase in the computational time involved in generating our stimuli. So, at this point, we decided to enlist the help of the University of Iowa's [high-performance computing cluster](https://hpc.uiowa.edu/). Using a distributed approach, we were able to generate our images in *hours instead of days*. The results were better than I had hoped for (see figure below).

{% include figure.html url="https://cloud.githubusercontent.com/assets/15203083/21275286/b24b5ede-c391-11e6-8ae9-a3a71f14ba87.gif" caption="Animated, multi-dimensional face-space (with 8 different faces on the spokes and the average on the hub)." width="70%" %}

---

### Voice-morphing -- ***Fall 2016*** -- [GH repo](https://github.com/meccaLeccaHi/voice_morphing)
After beginning my post-doc, I also became interested in understanding how the brain represents different identities of voices, which, despite being less informative than faces, are still a hugely important cue to help us to determine a person's identity.
In order to achieve test this, we planned to take the same approach we did with faces, but needed a completely different tool to morph between voices.

Enter [Hideki Kawahara](http://www.wakayama-u.ac.jp/~kawahara/index-e.html), who was on sabbatical at Google UK at the time and had agreed to collaborate on our project.
Dr. Kawahara had determined the most important acoustic features in discriminating between voices of different identities, and had created an algorithm to projects every voice into a reduced space, based on these dimensions (link [here](http://www.wakayama-u.ac.jp/~kawahara/STRAIGHTadv/index_e.html), *awesome* demo [here](https://youtu.be/vxiOu1HwQ-k?t=16)).

The code for this tool was written in MATLAB, so we decided not to use an open-source language to generate this stimuli. For the voices themselves, I enlisted the services of several different voice-over actors through the website [Fiverr](https://www.fiverr.com/), to impersonate the celebrity voice of my choosing (Arnold Schwarzenegger, Barack Obama, etc.). I really couldn't have been more pleased with the results (see below).

{% include figure.html url="https://camo.githubusercontent.com/5da33cc0e49f4009465410603d0c15c2ea974f11/687474703a2f2f692e696d6775722e636f6d2f3233434a5935362e706e67" caption="Multi-dimensional voice-space (with 8 different voices on the spokes and the average on the hub)." width="70%" %}

{% include youtubePlayer.html id="N6N1gfzqQZA" %}

---

### Gaming/Eye-Tracking with Python -- ***Spring 2017*** -- [GH repo](https://github.com/meccaLeccaHi/py_stimuli)
I would have to recommend creating a video game for anyone who loves old video games or Python. Fortunately for me, both are true.

This was actually really nostalgic. Unlike monkeys, human patients get bored *very easily*. I needed to make a "fun", "gamified" platform for our neuroscience studies. So, naturally, I decided to use leverage the sound effects, storylines, and transition effects from some of my childhood favorites (including): Punch-Out!!, Super Mario Bros., Base-Wars, and of course, GoldenEye.
This project relies heavily on [Psychopy](http://www.psychopy.org/), for presentation and timing and [PyGame](http://www.pygame.org/) for controls (mainly). Although we initially tried this using fancy eye-tracking software, ultimately, we discovered the good ol' X-Box controller to [work flawlessly](https://github.com/FRC4564/Xbox) and be way less of a pain for participants (thanks Microsoft!). Both the patients and I had a lot of fun with this one. We even got ≈25% greater participation by the pediatric patients, which put a smile on my face :) I believe this one speaks for itself -- check it out below.

{% include youtubePlayer.html id="Fa7tWZQfb8c" caption="Clips of the action from the hot new game: 'LazerMorph'!" %}

---

### Perceptual Studies via AWS Mechanical Turk -- ***Summer 2017*** -- [GH repo](https://github.com/meccaLeccaHi/mech_turk)

When given the choice between collecting data from college freshman one-by-one or anonymous internet users hundreds or thousands at a time, it was easy to choose the latter. Although it required a little elbow-grease (see excellent [tutorial](https://bradylab.ucsd.edu/ttt/)), the time and money required to gather data with this approach was reduced by more than 90%.

{% include figure.html url="https://camo.githubusercontent.com/22c2049faf1f36ee5e7670e43ccebeed19355db4/687474703a2f2f692e696d6775722e636f6d2f4662795369754b2e706e673f31" caption="Face similarity experiment, via Amazon mTurk." width="70%" %}

In order to visualize the perceived similarity (or *dis*-similarity) of these faces using the survey data we collected, we performed a simple form of dimensionality reduction using MDS. MDS is a useful way to visualize high-dimensional distance (or “dissimilarity”) data in a few dimensions — usually only two, for ease of visualization (see below).

{% include figure.html url="../assets/images/projects/face_mds.png" caption="Normalized responses of mTurk workers are shown projected in the same 2-dimensional space following classical MDS." width="65%" %}

---

### Record Linkage -- ***Fall 2017*** -- [GH repo](https://github.com/meccaLeccaHi/record_linkage)
As my first major gig outside of academia, I spent a lot of time surveying the literature for this one, and I learned a *lot* as a result. RL turned out to be a great area for me to work in as it has rich history and methodology going back as long people have been trying to keep track of each other (genealogy, censuses, etc.). Consequently, there is a rich literature dedicated to the topic, including both well-established probabilistic approaches and more modern modern approaches using single- and multi-layer neural networks, just to name a few.

RL also has a few ***characteristic issues*** that routinely require attention including:
- Substantial class imbalances (number of non-matches *far* exceeds the number of matches). For this issue, it's important to make sure you're not using the false-negative rate when assessing model performance.
- There's a *huge* number of potential Cartesian pairs to compare to test each possible match, so we *maximize pairing* with the [Kuhn-Munkres](https://pypi.python.org/pypi/munkres/) (i.e. Hungarian) Algorithm.
- Research with HIPAA-protected data requires patient de-identification, making matching more challenging.
In our case, we trained neural networks to match records across multiple SQL databases using ’fuzzy’ matching, resulting in a **≈75% reduction in non-matched records**. As a result, we were able to improve the accuracy of a medical record linkage system providing clinical performance metrics to *more than 200 hospitals*.

---

### Image Classification -- ***Spring 2018*** -- [GH repo](https://github.com/meccaLeccaHi/fed_detect)
This was my first exposure to the super-trendy and constantly-evolving world of image classification. As I found out, when big deal AI researchers want to make a name for themselves, they sometimes compete in high-profile, annual competitions such as [ImageNet](https://www.kaggle.com/c/imagenet-object-localization-challenge) and tend to involve the application of highly-complicated, non-linear models. As a result, developments in this field can take place rapidly -- just getting up to speed can be challenging!

Fortunately, a relatively large amount of attention has been paid to this subject, so the opportunities to learn about it are plentiful (e.g. [fast.ai](https://www.fast.ai/)). Around the same time, I had been trying my luck with some [Kaggle](https://www.kaggle.com/) competitions along the same lines (see my notebooks [here](https://github.com/meccaLeccaHi/kaggle)).

Critical Juncture, meanwhile, has created and maintains an online version of the [Federal Register](https://www.federalregister.gov/), which is a publication that provides access to the official text of federal laws, presidential documents, etc for a given day in the U.S. Since the federal government has only recently digitized the archived content, none of the figures before a certain date (say, 1995) were able to be indexed quickly and/or easily.

In order to improve the overall readability and discoverability of decades of government documents, we set out to **train two image classification models: one for *semantic category* and one for the *rotation* of figures** embedded in the digital archives of the Federal Register. Each model consists of a pre-trained convolutional neural network with drop-out, and a partially un-frozen convolutional base, and **perform with very high (>98%) accuracy.** I attribute this to a couple things:
1. The similarity between different classes is low (see figure below), which presumably made it easier for the model to learn to distinguish between them.
{% include figure.html url="https://camo.githubusercontent.com/695b3b2aafe3ece038296095e87f2792ad6a47fc/68747470733a2f2f692e696d6775722e636f6d2f656a63367774592e706e673f31" caption="Semantic-category class examples." %}
2. Like other [examples](https://arxiv.org/pdf/1603.08511.pdf), predicting image rotation has the nice property of being practically "free": any image can be used as a training sample, simply
by rotating the image as input and using the rotation as the supervisory signal.
{% include figure.html url="https://camo.githubusercontent.com/4c72814164f684462451b9b1c03428bc7cc0c871/68747470733a2f2f692e696d6775722e636f6d2f324946763358542e706e673f31" caption="Image-rotation class examples." %}

Because this problem was *so* well suited to image classification, our models performed with *extremely high accuracy* (**>98%**, see examples below).
{% include double_figure.html url1="https://camo.githubusercontent.com/aa07576b4f9da35caf829c1b53b0ba69e9fbd27d/68747470733a2f2f692e696d6775722e636f6d2f6548656a75395a2e706e67" width1="35%" width2="30%"  url2="https://camo.githubusercontent.com/249d6d81fae9779f219f30080d9f6fd0d3bcbd4d/68747470733a2f2f692e696d6775722e636f6d2f7a6959686e6b692e706e67" caption="Semantic-category (left) and image-rotation (right) prediction examples." %}

---

### Python Apps:
#### Snowblog! -- ***Fall 2018*** -- [GH repo](https://github.com/meccaLeccaHi/snowblog)  
[Heroku link](https://snowblogg.herokuapp.com/index)

This was a fun way to learn web-dev in Python ([Flask](http://flask.pocoo.org/), specifically), as well as a good excuse to learn which ski resorts I needed to visit and where they were located.
This app uses two data sources:
1. Pre-scraped data from [OpenSnow.com](https://www.opensnow.com), including the name and state/province of every ski resort in America and Canada, housed in a SQLite database.
2. API calls to [Google Geocode](https://developers.google.com/maps/documentation/geocoding/start) via [`googlemaps`](https://github.com/googlemaps/google-maps-services-python) (a Python client library), allowing the retrieval of the latitude and longitude of each resort, as well as that of the user.

With that, this app finds the ski resorts with the lowest euclidean distance, and displays those to the user. It also provides a database for storing information on each resort following your visit.

#### FreshyFinder -- ***Fall 2018*** -- [GH repo](https://github.com/meccaLeccaHi/snow_scraper)  
[Heroku link](https://snowscraper.herokuapp.com/)

With this one, I wanted to focus more heavily on visualizations, specifically. So, I decided to incorporated [Plotly Dash](Plotly Dash) into my Flask app, as well as more map-specific plotting tools, such as [MapBox](MapBox). Since more elaborate data was required for this project, I relied more heavily on [BeautifulSoup]() than I have in past projects (see [blog post](./webscraping/) for more info).

---

### pyAL: Cyborg moths  -- ***Currently underway*** -- [GH repo](https://github.com/meccaLeccaHi/pyAL)  
[Source](https://github.com/charlesDelahunt/PuttingABugInML)

[[*Description goes here.*]]
