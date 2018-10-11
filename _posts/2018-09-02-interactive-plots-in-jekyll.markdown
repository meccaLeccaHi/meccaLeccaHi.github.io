---
title:  "Adding interactive plots to a Jekyll blog"
date:   2018-09-02
layout: post
tag:
- python
- jekyll
- music
- lyrics
category: blog
author: john
name: john
image: assets/images/Plot_like_love.png
description: Interactive plots from Python in a Jekyll blog
---
I've been trying for awhile to get interactive plots going on my Jekyll blog. It turns out you can export plots from `matplotlib` in Python to HTML using a handy library called [`mpld3`](https://mpld3.github.io/).

## Example interactive plot
After analyzing 12k+ [country lyrics](http://www.johnwmillr.com/trucks-and-beer/), I've gone and downloaded about 40k rap and rock lyrics using my [LyricsGenius](https://github.com/johnwmillr/LyricsGenius) Python package. I'm still working on my analysis of those lyrics, but I think this first plot is pretty interesting.

Move your mouse over the points in the plot to see more detail about the artists they represent.

{% include plot_like_love.html %}

For whatever reason, measuring how often an artist uses the word *like* is a pretty decent way to differentiate between country, rock, and rap artists. Rap artists are much more likely than country artists to use the word *like* in their songs.

There is also a clear separation on gender between country artists for the word *love*, but the effect doesn't appear to hold for rap artists. Unfortunately, there weren't enough female rock artists in my dataset to notice any relationships with gender in that genre.

### Creating the plot
As I mentioned above, I used the `mpld3` library to make the interactive plot. The library went unmaintained for awhile, but has been [recently](https://github.com/mpld3/mpld3/commit/c490724928f827721c0d4389c742e4c4ae8fab27) switched to new maintainers, which will hopefully revitalize the project. Before this switch in ownership, I [forked](https://github.com/johnwmillr/mpld3) the repo to continue making small tweaks to suit my needs.

The process of creating an interactive plot with `mpld3` is actually fairly straightforward. The library is well documented and provides a number of helpful [tutorials](https://mpld3.github.io/quickstart.html) and [examples](https://mpld3.github.io/_downloads/mpld3_demo.html) for getting started. I use the library's [tooltip](https://mpld3.github.io/examples/html_tooltips.html) feature with some extra CSS to make the artist info and image show up on the plot above.

Here is the relevant code excerpt from the tooltip tutorial:
```python
fig, ax = plt.subplots(figsize=(10,10))

labels = []
for i in range(N):
    label = df.ix[[i], :].T
    label.columns = ['Row {0}'.format(i)]
    labels.append(str(label.to_html()))

points = ax.plot(df.x, df.y, 'o', color='b',
                 mec='k', ms=15, mew=1, alpha=.6)

tooltip = plugins.PointHTMLTooltip(points[0], labels,
                                   voffset=10, hoffset=10, css=css)
plugins.connect(fig, tooltip)
mpld3.show()
```

Using the `mpld3.show()` function will display the graph within a Jupyter notebook. However, we're interested in exporting the plot for use in a Jekyll blog post, so we'll use the `mpld3.save_html()` function instead of the `show()` command:

```python
filename = 'example_plot.html'
mpld3.save_html(fig, filename, template_type='simple')
```

For some reason, the plot wouldn't render in my blog post unless I set the `template_type` variable to `'simple'`.

### Adding the plot to a post
After exporting the plot as an HTML file, add it to the `_includes/` directory within your Jekyll site. After putting the file in place, we just need to include the HTML within the Markdown file for a blog post:

```html
Here is some example text for an exciting blog post. Deep blockchain learning is the future, blah, blah, etc.

{{ "{% include example_plot.html " }}%}

And then you keep writing your exciting blog post.
```

That's it! The interactive plot should show up once the Jekyll site is built and renders the page.

## Up next
I'd love to make the plots even more interactive. It would be very cool if users were able to specify the actual lyrics data that gets displayed in the plot. If anybody knows a way to do this with a Jekyll blog, let met know!
