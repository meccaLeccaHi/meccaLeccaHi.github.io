---
title:  "Pitchfork album reviews"
date:   2018-06-05
layout: post
tag:
- python
- music
- lyrics
category: blog
author: john
name: john
image: assets/images/lexdiv_album_reviews.png
description: Comparing Pitchfork album reviews and song lyrics
---

I've been scraping Pitchfork reviews using Michal Czaplinski's excellent [Python wrapper](https://github.com/michalczaplinski/pitchfork) for the [Pitchfork](https://pitchfork.com/) music website. I've searched through my collection of [rap, rock, and country lyrics](http://www.johnwmillr.com/interactive-plots-in-jekyll/) and scraped reviews for albums that were reviewed on Pitchfork.

The plot below compares the relationship between the [lexical diversity](https://en.wikipedia.org/wiki/Lexical_diversity) of an album's lyrical content and the review score the album received on Pitchfork. Move your mouse over the points in the plot to see more detail about the albums they represent.

{% include mpld3_lexdiv_vs_score.html %}

I was surprised to find a small negative correlation between the album review score and the lexical diversity of the album's corresponding review. The Pitchfork reviews for higher-rated albums are less lexically diverse.

{% include mpld3_score_vs_lexdiv_reviews.html %}

Here's a prettier, static version of the same plot:

[![Album review lexical diversities](/assets/images/lexdiv_album_reviews.png){: .center-image }](https://www.reddit.com/r/dataisbeautiful/comments/9hmtcm/lexical_diversity_of_pitchfork_album_reviews/)
