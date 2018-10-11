---
title: "Unix to the rescue!"
date: 2018-08-20
layout: post
tag:
- python
- data science
- unix
category: blog
author: john
description: Using Unix to process 200k+ files
---

I've been working on a data science project that involves analyzing food recipes downloaded from the Internet. I found one dataset floating around the web that contains over 200,000 recipes scraped from [Allrecipes](http://allrecipes.com/) and was available in two different versions. The first version was stored in JSON format and had already been cleaned and organized. The second version of the dataset contained the raw HTML for each of the 200k+ recipes, and in its least-compressed form, took up about 40 gigabytes of space.

The odd thing about this dataset is that roughly 60% of its 200k+ recipes are identical. For whatever reason, there are more than 120,000 copies of a [*Johnsonville Three Cheese Italian Style Chicken Sausage Skillet Pizza*](https://www.allrecipes.com/recipe/219661/johnsonville-three-cheese-italian-style-chicken-sausage-skillet-pizza/) recipe.

{% include figure.html url="https://images.media-allrecipes.com/userphotos/720x405/995905.jpg" caption="The Chicken Sausage Skillet Pizza, presented without comment." width="80%" %}

Why there are so many copies of this recipe -- or, for that matter, why the dish exists in the first place -- is beyond me. I was more concerned with how all the duplicate recipes would affect my analysis.

## The task at hand
As part of my food recipes project, I'm interested in finding different versions of recipes for the same type of food (e.g. chocolate chip cookies) and comparing how the combinations of ingredients vary between recipes. To properly compare different recipes I need to know how many servings each is supposed to make. For example, two different cookie recipes may both require a cup of sugar, but you'll end up with completely different cookies if the first recipe is for a batch of ten while the second makes three dozen.

{% include figure.html url="/assets/images/lotsOfFiles.gif" caption="Files for days!" width="100%" %}

Unfortunately, the recipes in the pre-cleaned JSON dataset did not contain serving size information. The raw HTML files did contain serving sizes, but I would have to iterate through each of the 200k+ files to extract the information. I knew my work would be considerably faster if I could throw out the duplicate *Johnsonville* recipes and reduce the size of my dataset by 60%.

## Python approach
My first instinct was to write a simple Python script to iterate through the HTML files and delete any that contained the *Johnsonville* recipe. The code itself was easy enough to write. I got a Jupyter notebook going that looped through the raw HTML files, deleted any *Johnsonville* duplicates, and estimated the script's remaining time.

```python
# Loop through the HTML recipe files, deleting the Johnsonville duplicates
import os, time

def calcTimeRemaining(elapsed, n, total):
    return (total-n)/(n/elapsed)

htmlFiles = os.listdir('./Data/Recipes/O2/recipes_html/')
numFiles = len(htmlFiles)
start = time.time()
last = time.time() - start
for n, filename in enumerate(htmlFiles):
    with open(filename, 'r') as infile:
        html = infile.read()
    if 'italian style chicken sausage skillet pizza' in html:
        os.remove(filename)
    if (time.time() - last)/60 > 0.05:  # Print a progress update
        last = time.time()
        elapsed = (time.time() - start)/60
        print("File ({n}/{t}) | Remaining: {r:.1f} min | Files/min: {fpm:.1f}".format(
            n=n+1, t=numFiles, fpm=(n+1)/elapsed,
            r=calcTimeRemaining(elapsed, n+1, numFiles)))
```

After letting the Jupyter notebook run for a few minutes, I was shocked to see an estimated 12 hours remaining.
```
File (1531/225624) | Remaining: 12.1 hours | Files/min: 303.1
```

There had to be a better way!

## Unix to the rescue
My moment of clarity came while listening to DataCamp's [*DataFramed*](https://www.datacamp.com/community/podcast/kaggle-future-data-science) Podcast in the shower. Hugo Bowne-Anderson, the show's enthusiastic host and interviewer, was doing a *Language Corner* interlude with Spencer Boucher, a Data Science Curriculum Lead at Data Camp, about the often overlooked utility of Unix in data science. Hugo and Spencer stressed a few key advantages command-line tools have over full-featured programming languages when it comes to data science work:

- Most Unix tools have rich APIs, optimized for the "80% use case" (i.e. optimal commands for one-off tasks)
- Unix is available in nearly all scientific computing environments, even when full programming languages aren't
- Unix tools can be easily chained together to create powerful, sophisticated commands
- Using Unix can help avoid loading entire datasets into memory for processing
- Many Unix commands are easily parallelizable

During Spencer's call to action to use Unix tools for data science (especially while cleaning data) it hit me -- I could use Unix to delete the *Johnsonville* recipes!

A quick Google search led me to a Stack Overflow [post](https://stackoverflow.com/questions/4529134/delete-files-with-string-found-in-file-linux-cli) that recommended piping the output of a `grep` command into `awk`, creating an executable `.sh` file that would then delete the duplicate recipes. After visiting a few more Stack Overflow forums and testing the commands in a directory with fewer files, I ended up with a string of commands that did the trick:

<a name="full-unix-command"></a>
```shell
$grep -rl . -e 'Italian Style Chicken Sausage Skillet Pizza' | awk '{print "rm -v "$1}' > deleteRecipes.sh
$source deleteRecipes.sh
```

I've added an [appendix](#complete-description) to this post that provides a full description of how each of the Unix tools are working together in the command above.

## Summary
The whole process of identifying and deleting the culprit recipes took about 1.5 hours with the Unix code above, nearly 90% faster than the estimated time for my Python code! There are bound to be better solutions to this problem than the ones I've described here. I'm sure there's a proper way to solve this sort of problem in Python, and I'd love to hear in the comments below what approach that may be.

But for me, this was a great opportunity to try out a new technique and expand my set of data science skills ever so slightly. The next time I'm tackling a 40 GB list of unruly HTML files, I'll be less likely to chuck my keyboard across the room in frustration and more quick to pull this powerful `grep` `awk` combo from my data science tool belt.

A big thanks to Hugo and Spencer from the [*DataFramed*](https://www.datacamp.com/community/podcast) Podcast. If you aren't already listening to *DataFramed*, I strongly recommend checking it out. Each episode covers a different area of data science, and Hugo is an engaging, articulate interviewer.

**Update**:
Guess I should have done a bit more Googling and just used [`fdupes`](https://github.com/adrianlopezroche/fdupes). 😑

---

<a name="complete-description"></a>
## Appendix
### Full description of the Unix tools [⇪](#full-unix-command)
The Unix code I ended up with makes use of a couple of really helpful command-line tools:

[`grep`](https://www.computerhope.com/unix/ugrep.htm)

 The `grep` tool uses [regular expressions](https://en.wikipedia.org/wiki/Regular_expression) to parse and print text within the command line. In the command above I'm telling `grep` to search the current directory for any files containing the "Skillet Pizza" text and to then print their file names.

 The `-rl` option tells `grep` to search recursively and print the matched file names, rather than the actual matched text. The `e` option is used to specify the regular expression to search with. The `.` tells `grep` to search within the current directory.

[`pipe`](http://www.linfo.org/pipes.html) and [`redirect`](http://www.westwind.com/reference/os-x/commandline/pipes.html#redir-output)

The `|` character in-between the `grep` and `awk` commands is a *pipe* and is used to send the output from one command into another. The `>` character redirects the output of a command to be stored as text in a file (and vice versa). In my example above, the output from `grep` (a list of filenames) is piped into the `awk` command whose output (a list of `rm` commands) is then redirected into the `deleteRecipes.sh` file. Be careful with `>` as it will overwrite any existing files with the same name. The `>>` operator is a safer alternative that appends to rather than overwrites existing files.

[`awk`](http://linuxcommand.org/lc3_adv_awk.php)

The `awk` command is actually calling an entire programming language (named AWK) that is helpful for filtering text, especially data stored in a columnar format (e.g. `CSV`). Serendipitously, my friend [Micah](http://micahjon.com/) sent me a [helpful article](https://gregable.com/2010/09/why-you-should-know-just-little-awk.html) while I was working on this post that makes a case for learning AWK and provides a few useful examples.

I'm using `awk` to generate a line of text -- `rm -v FILENAME.html` -- for each *Johnsonville* recipe identified by `grep`. The `$1` is a variable in `awk` that will take on the file names piped in from `grep`. The `rm` statement deletes the specified file, and `-v` makes the command verbose.

"`argument list too long`"

Because the directory I was working in contained so many files, I kept running into an "`argument list too long`" error when I would try the command I found on the original Stack Overflow post. Unix has a limited buffer for the length of any given command, and so it was unable to string together the roughly 120,000 names of files containing the *Johnsonville* recipe. In the end, outputting the `rm` commands to a file to be executed later (rather than maintaining a list of all the `rm` within the command line buffer) allowed me to get around the error.

Finally, I call use the [`source`](https://bash.cyberciti.biz/guide/Source_command) command to run the `rm` commands and delete the offending *Johnsonville* recipes.
