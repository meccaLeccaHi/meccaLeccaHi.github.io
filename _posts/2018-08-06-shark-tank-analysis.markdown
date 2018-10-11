---
title: "Swimming in the Shark Tank… 🦈 Does gender matter?"
date: 2018-08-06
layout: post
tag:
- python
- data science
category: blog
author: john
image: assets/images/sharktank_main_graph.png
description: There are gender imbalances in the deals made on Shark Tank, but that doesn’t mean the Sharks are sexist.
---

This is a piece I originally wrote for the Dig3st data science blog on [Medium](https://medium.com/dig3st/swimming-or-sinking-in-the-shark-tank-does-gender-matter-aafa88180f7). It must be at least halfway decent, because [Mark Cuban](https://twitter.com/mcuban) liked my post on Twitter! Still waiting for him to get back to me about a data scientist job with the Mavs...

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Finished my <a href="https://twitter.com/hashtag/DataVisualization?src=hash&amp;ref_src=twsrc%5Etfw">#DataVisualization</a> post about <a href="https://twitter.com/hashtag/SharkTank?src=hash&amp;ref_src=twsrc%5Etfw">#SharkTank</a>. Looked at each Shark&#39;s funding history, broken down by gender. <a href="https://twitter.com/BarbaraCorcoran?ref_src=twsrc%5Etfw">@BarbaraCorcoran</a> and <a href="https://twitter.com/robertherjavec?ref_src=twsrc%5Etfw">@robertherjavec</a> are the most biased! <a href="https://twitter.com/mcuban?ref_src=twsrc%5Etfw">@mcuban</a> and <a href="https://twitter.com/TheSharkDaymond?ref_src=twsrc%5Etfw">@TheSharkDaymond</a> are pretty fair. <a href="https://twitter.com/hashtag/DataScience?src=hash&amp;ref_src=twsrc%5Etfw">#DataScience</a><a href="https://t.co/G7LbXDmpCy">https://t.co/G7LbXDmpCy</a></p>&mdash; John W. Miller (@johnwmillr) <a href="https://twitter.com/johnwmillr/status/1026359202749526016?ref_src=twsrc%5Etfw">August 6, 2018</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

---
## Introduction

My brother and I are big fans of [Shark Tank](https://abc.go.com/shows/shark-tank). After watching a few episodes together on vacation recently, I started to wonder whether it’d be possible to identify any patterns in the way Sharks make deals on the show. For instance---*are male Sharks more likely to make deals with men than women?* Or, for that matter, *are male entrepreneurs more likely to make it on the show in the first place?* With a few of these questions in mind, I started looking for the data I’d need to come up with answers.

## Collecting the data
As I suspected, I wasn't the first to ask these sorts of questions about Shark Tank. In a post on Quora, [Halle Tecco](https://twitter.com/halletecco) described her own [detailed analysis](https://www.quora.com/What-have-you-learned-from-watching-the-television-program-Shark-Tank/answer/Halle-Tecco) of the show. Amongst other insights, Halle found that across the first six seasons of the show, the two female Sharks (Barbara Corcoran and Lori Greiner) made a larger percentage of their deals with women than their male counterparts.

Halle made the data she collected available [online](https://docs.google.com/spreadsheets/d/1Lr0gi_QJB_JU0lBMjJ7WiBRxA0loml1FlM-KlmKsaEY/edit#gid=0). Due to a lack of information in the dataset on entrepreneurs with non-binary gender identity, I only used male and female labels in my analysis. The code I wrote for this analysis is available on [GitHub](https://github.com/johnwmillr/SharkTank).

## Posing the question
It’s worth noting that the number of men and women appearing on the show is not equal: the ratio of all-male teams to all-female teams is roughly 70/30.

![Gender representation on *SharkTank*](/assets/images/sharktank_gender_ratios.png){: .center-image }

I was curious to see how each Shark’s funding probabilities might look after accounting for this skewed ratio. As I thought through different ways to measure this effect, I kept asking myself the same question — *what percentage of pitches from either gender did each Shark make a deal with?*

![Funding probability metric](/assets/images/sharktank_metric.png){: .center-image }

I needed a bit more data to be able to answer my question. Luckily, there is a [Wikipedia page](https://en.wikipedia.org/wiki/List_of_Shark_Tank_episodes) that provides short descriptions of each Shark Tank episode. I used [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) to [scrape](https://github.com/johnwmillr/SharkTank/blob/master/scrapeSharkTankData.ipynb) the attendance records for each of the main Sharks on the show. By combining Halle’s deal data with the attendance records I collected, I was able to determine how often each Shark made deals with the male and female entrepreneurs they heard pitches from.

[![Funding on *SharkTank* by gender](/assets/images/sharktank_main_graph.png){: .center-image }](https://www.reddit.com/r/dataisbeautiful/comments/8wr8ko/funding_probabilities_on_shark_tank_grouped_by/)

Each bar represents the percent of entrepreneurs of a given gender that the Shark made deals with. For example, Mark Cuban made deals with 20.2% of the women and 17.1% of the men he heard pitches from.

## Discussion
The main conclusion to draw from the graph is that certain Sharks do not make deals with men and women at equal rates. The next step is to ask what might be contributing to this imbalance. The wrong step is to jump to the conclusion that the Sharks are acting on sexist motivations.

Clearly, there are many factors at play here. For one, Barbara Corcoran and Robert Herjavec — the Sharks with the largest funding biases — tend to invest in completely different industries (food/beverage and tech, respectively). Additionally, the data I collected do not contain information on which Sharks made offers that were rejected, meaning my graph does not account for potential biases on behalf of the entrepreneurs.

Season 10 of Shark Tank premiers this October. ABC’s [promo](https://abc.go.com/shows/shark-tank/news/updates/shark-tank-season-10-premiere-date-time) for the show claims that “[The Sharks] will once again give people from all walks of life the chance to chase the American dream”. I’m looking forward to the premiere as much as anyone else. But with this analysis in mind, I’ll think a bit more about who gets to walk onto the show — and leave with a deal.
