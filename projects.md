---
layout: page
title: Projects
category: project
---

<h1 class="title">{{ page.title }}</h1>

<section class="list">

</section>

> You can find most of my work on [GitHub](https://github.com/meccaLeccaHi). Several posts on my [blog](blog/) are also related to these projects.
> Please feel free to leave a comment below.

---

### Face-morphing with ANTs -- ***Spring 2016***
[GitHub repo](https://github.com/meccaLeccaHi/face_morphing)
This was the first project that got me really hooked on the exciting possibilities in open-source programming.
Starting in grad school, I had been on the lookout for a method of morphing faces without the tedium of manually-placing hundreds of 'points' on each face.
Quite unexpectedly, I found that I was able to get really good results using image segmentation tools ([ANTs](http://stnava.github.io/ANTs/), namely), which had actually been designed application to MRI images of the brain. Here was a tool that excelled at unsupervised alignment of anatomical brain scans, and we were able to use it (quite successfully) to align (and transition between) different faces. This worked really well for morphing between stationary faces (see figure below), but our main interest was in using 'life-like' clips of moving, talking faces.

{% include figure.html url="https://camo.githubusercontent.com/ef03ccb71de920c61fb5d4e96afdba923c91cb4c/687474703a2f2f692e696d6775722e636f6d2f3476683858784b2e706e67" caption="Face morphing via image segmentation and alignment." width="70%" %}

Soon after, I began a collaboration with [Supasorn Suwajanakorn](http://www.supasorn.com//), then at Washington University. He had created these really nice controllable models of a handful of different celebrities (link [here](http://grail.cs.washington.edu/projects/3DPersona/)). With them, we were prepared to apply the same segmentation technique to each frame of a short video.

Obviously, this required a substantial increase in the computational time involved in generating our stimuli. So, at this point, we decided to enlist the help of the University of Iowa's [high-performance computing cluster](https://hpc.uiowa.edu/). Using a distributed approach, we were able to generate our images in *hours instead of days*. The results were better than I had hoped for (see figure below).

{% include figure.html url="https://cloud.githubusercontent.com/assets/15203083/21275286/b24b5ede-c391-11e6-8ae9-a3a71f14ba87.gif" caption="Animated, multi-dimensional face-space (with 8 different identities on the *spokes* and the average on the *hub*)." width="70%" %}

---

### Voice-morphing with STRAIGHT -- ***Fall 2016***
[GitHub repo](https://github.com/meccaLeccaHi/voice_morphing)
After beginning my post-doc, I also became interested in understanding how the brain represents different identities of voices, which, despite being less informative than faces, are still a hugely important cue to help us to determine a person's identity.
In order to achieve test this, we planned to take the same approach we did with faces, but needed a completely different tool to morph between voices.

Enter [Hideki Kawahara](http://www.wakayama-u.ac.jp/~kawahara/index-e.html), who was on sabbatical at Google UK at the time and had agreed to collaborate on our project.
Dr. Kawahara had determined the most important acoustic features in discriminating between voices of different identities, and had created an algorithm to projects every voice into a reduced space, based on these dimensions (link [here](http://www.wakayama-u.ac.jp/~kawahara/STRAIGHTadv/index_e.html), *awesome* demo [here](https://youtu.be/vxiOu1HwQ-k?t=16)).

The code for this tool was written in MATLAB, so we decided not to use an open-source language to generate this stimuli. For the voices themselves, I enlisted the services of several different voice-over actors through the website [Fiverr](https://www.fiverr.com/), to impersonate the celebrity voice of my choosing (Arnold Schwarzenegger, Barack Obama, etc.). I really couldn't have been more pleased with the results (see below).

Spectrograms of voices in multi-dimensional space.[](https://camo.githubusercontent.com/5da33cc0e49f4009465410603d0c15c2ea974f11/687474703a2f2f692e696d6775722e636f6d2f3233434a5935362e706e67)
> Faces and voices [combined](https://youtu.be/N6N1gfzqQZA).

{% include youtubePlayer.html id="N6N1gfzqQZA" %}

---

### Gaming/Eye-Tracking with Python -- ***Spring 2017***
[GitHub repo](https://github.com/meccaLeccaHi/py_stimuli)
I would have to recommend creating a video game for anyone who loves old video games and/or wants to learn Python. Fortunately for me, I'm both! 

This was actually really nostalgic. I needed to make a "fun", "gamified" platform for our neuroscience studies. So, naturally, I decided to use sound effects and transitions from some of my childhood favorites, including: Punch-Out!!, Super Mario Bros., Base-Wars, and of course, GoldenEye.
This project relies heavily on [Psychopy](http://www.psychopy.org/), for presentation and timing and [PyGame](http://www.pygame.org/) for controls (mainly). Although we initially tried this using fancy eye-tracking software, ultimately, we discovered the good ol' X-Box controller to [work flawlessly](https://github.com/FRC4564/Xbox) and be way less of a pain for participants (thanks Microsoft!). Both the patients and I had a lot of fun with this one. I believe this one speaks for itself -- [check it out](https://youtu.be/Fa7tWZQfb8c).

Clip from *Laser Morph*.[](https://youtu.be/Fa7tWZQfb8c)
{% include youtubePlayer.html id="Fa7tWZQfb8c" %}

---

### Record Linkage -- ***Fall 2017***
[GitHub repo](https://github.com/meccaLeccaHi/record_linkage)
As my first major gig outside of academia, I spent a lot of time surveying the literature for this one, and I learned a lot as a result.

---

### Image Classification -- ***Spring 2018***
[GitHub repo](https://github.com/meccaLeccaHi/fed_detect)


---

### Python Apps:
#### Snowblog! -- ***Fall 2018***
[GitHub repo](https://github.com/meccaLeccaHi/snowblog)
[Heroku link](https://snowblogg.herokuapp.com/index)


#### FreshyFinder -- ***Fall 2018***
[GitHub repo](https://github.com/meccaLeccaHi/snow_scraper)
[Heroku link](https://snowscraper.herokuapp.com/)


---

### pyAL: Cyborg moths  -- ***Currently underway***
[GitHub repo](https://github.com/meccaLeccaHi/pyAL)
[Source repo](https://github.com/charlesDelahunt/PuttingABugInML)
