---
title:  "Trucks and beer 🍺"
date:   2018-02-07
layout: post
tag:
- python
- data science
- music
- lyrics
category: blog
author: john
name: john
image: assets/images/FreqPlot_beer_and_truck.png
description: Analyzing country music lyrics
---

Inspired by a post on [Big-ish Data](https://bigishdata.com/2016/10/25/talkin-bout-trucks-beer-and-love-in-country-songs-analyzing-genius-lyrics/), I've started working on a textual analysis of popular country music.

More specifically, I scraped Ranker.com for a list of the top female and male country artists of the last 100 years and used my [python wrapper](https://github.com/johnwmillr/LyricsGenius) for the Genius API to download the lyrics to each song by every artist on the list. After my script ran for about six hours I was left with the lyrics to 12,446 songs by 83 artists stored in a 105 MB JSON file. As a bit of an outsider to the world of country music, I was curious whether some of the preconceived notions I had about the genre were true.

Some pertinent questions:
  - Which artist mentions trucks in their songs most often?
  - Does an artist's affinity for trucks predict any other features? Their gender for example? Or their favorite drink?
  - How has the genre's vocabulary changed over time?
  - Of all the artists, whose language is most diverse? Whose is most repetitive?

You can find my code for this project on [GitHub](https://www.github.com/johnwmillr/trucks-and-beer).

---
# Analysis

## If you like beer, you may also like...
I'm interested in whether an artist's tendency to use certain terms correlate together. For example, if an artist is more likely to mention beer in their songs, are they more likely to also mention trucks?

It turns out that yes, they are.

Each point on the two plots below represents a single artist. The values for each point were calculated as the percentage of times the given artist mentions a particular term across all of their songs. For example, Cole Swindell had 46 total songs and mentioned beer in 24 of them, arriving at a percentage of 52%.

Think about that. [Cole Swindell](https://genius.com/artists/Cole-swindell) mentions beer in *more than half of his songs*. You can also count on him referencing trucks once every five songs. [Dustin Lynch](https://genius.com/artists/Dustin-lynch) turned out to be the artist that sang about trucks most frequently, with the word *truck* appearing in 23.8% of his songs.

![beer_and_trucks]({{site.url}}/assets/images/FreqPlot_beer_and_truck.png){: .center-image }

I've also added the artists' genders to the plot. I'll need to do some more analysis, but there does appear to be a relationship between an artist's gender and their tendency to sing about trucks and beer. It's hard to tell from this plot, but roughly half of the female artists in my dataset are actually stacked on top of each other at the origin, meaning they didn't mention beer or trucks in any of their songs.

Check out the relationship between an artist's use of the words *girl* and *love*. There's an even more obvious trend with gender here. The more often a male country singer uses the word *girl* in his songs, the less likely he is to mention *love*. Interesting.

![girl_and_love]({{site.url}}/assets/images/FreqPlot_girl_and_love.png){: .center-image }

## Love is falling out of fashion
I also wanted to look at how vocabulary changes over time for all country artists. We know from the plot above that male country artists are less likely to sing about love and more likely to sing about girls. The above plots combined songs from all years -- I wonder if we'll see different effects after separating songs into the years they were published.

The plot below displays the percentage of songs mentioning a given term for each year, excluding years that had less than ten songs in my database. It looks like it's becoming less common for country artists to sing about love. The correlation isn't all that strong, but there is a noticeable downward trend.

![vocab_over_time]({{site.url}}/assets/images/TimePlot_girl_boy_love.png){: .center-image }

I also found it funny that as *love* gets mentioned less frequently, it's becoming more common for country songs to include the word *girl*. And, if we remember from the plot of *girl* vs. *love* above, we know it's primarily men who are driving the rise in popularity of this term. The popularity of the word *boy* hasn't changed much over time, appearing in about 12% of songs each year.

## Country music is getting more repetitive

After reading Kaylin Walker's excellent post "[50 Years of Pop Music](http://kaylinwalker.com/50-years-of-pop-music/)", I decided to look at how vocabulary sizes have changed over time. Similar to what Kaylin found when looking at Bilboard hits from the last 50 years, it appears that, while the correlation is weak, the average total word count for country songs has increased with time. The average unique word count has also increased with time but only slightly.

[![vocabulary_size]({{site.url}}/assets/images/TimePlot_words_per_song.png){: .center-image }]({{site.url}}/assets/images/TimePlot_words_per_song.png)

In other words, country lyrics have become more repetitive over the years.

To dig a little deeper, I took a look at the [lexical diversity](http://www.nltk.org/book/ch01.html) of the lyrics over time. Lexical diversity is a fancy term for a simple concept: what percentage of the words in a body of text are unique? A body of text where each word is only used once would have the highest possible lexical diversity with a value of 1.

![lexical_diversity]({{site.url}}/assets/images/TimePlot_lexical_diversity.png){:class="center-image" height="80%" width="80%"}

Sure enough, if we look from year 2002 to the present (where the effect is most pronounced), there is a clear downward trend in lexical diversity. This trend holds for pop music in general, as illustrated by this [excellent post](https://pudding.cool/2017/05/song-repetition/) from The Pudding on the repetitive nature of pop lyrics. Might this be an indication that country music has gotten more poppy over time?

## And the most repetitive artist is...

At the start of this post I asked which artists have the most and least diverse lyrics. Lexical diversity can give us some insight into this question. For each artist, I calculated the average lexical diversity across each of their songs. The figure below shows the distribution of different lexical diversity values. The average country artist has a lexical diversity of 0.50. There would be a number of possible ways to arrive at 0.50, but one intuition for the value is that about half the words in a song are unique.

![lexical_diversity_histogram]({{site.url}}/assets/images/LexDiv_distribution.png){:class="center-image" height="80%" width="80%"}

So, to answer the question, "whose lyrics are most diverse?", we can just look at the extremes of the distribution. [Kane Brown](https://genius.com/artists/Kane-brown) comes in at the bottom with a lexical diversity score of 0.39, and [Kellie Pickler](https://genius.com/artists/Kellie-pickler) is sitting on top with 0.59. To try and get a sense for what the two artists sing about, I generated [word clouds](https://github.com/amueller/word_cloud) from their respective sets of lyrics.

[![word_cloud]({{site.url}}/assets/images/WordCloud_lexical_diversity.png){:class="center-image" height="100%" width="100%"}]({{site.url}}/assets/images/WordCloud_lexical_diversity.png)

It's difficult to draw much from the word clouds by themselves, but it's a fun way to get a quick impression of which words an artist uses most often. Kane Brown's favorite words are *girl*, *back*, *know*, and *yeah*. Kellie Pickler's are *love*, *know*, *want*, and *go*.

## Days of the week
[![livin_for_the_weekend]({{site.url}}/assets/images/BarGraph_Weekend.png)]({{site.url}}/assets/images/BarGraph_Weekend.png)

This one is pretty straightforward. Looks like we're all just livin' for the weekend.

## Making predictions
So, we've collected a bunch of country lyrics, and we've started to notice some interesting trends in the data. Can the trends we've identified provide any further insight into the genre? Might we be able to use the trends we've identified in the lyrics to make inferences about the artists? Could we, for example, given a set of song lyrics guess the gender of the artist who wrote them?

To make these sorts of predictions and inferences from the lyrics, we'll need to identify useful features and train a classifier, both of which I'll go into detail on in my next post. Stay tuned!
