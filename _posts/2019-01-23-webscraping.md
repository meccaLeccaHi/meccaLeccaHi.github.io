---
title: "Web Scraping Weather Data"
date: 2019-01-23
layout: post
math: false
category: blog
comments: true
tag:
- web scraping
- Beautiful Soup
- API
- Google Maps
author: adam
description: Post demonstrating the use of Beautiful Soup and Google Maps to collect weather forecast data.
---

# Web Scraping Weather Data

## Topic Guide
- [Learning Objectives](#learning-objectives)
- [Background](#background)
	- [Overview](#overview)
- [Part 1. Web Scraping with Beautiful Soup](#web)
	- [Installation](#installation)
	- [Example: Scraping a website](#scraping)
- [Part 2. Location Data with Google Maps API](#google)
	- [API Key](#key)
- [Summary](#summary)
    - [Further Study](#study)

<a id="learning-objectives"></a>
## Learning Objectives

- Recognize the types of problems web scraping is useful for.
- Observe an application of web scraping to an example web site.
- Determine how to apply web scraping to collect the data of your choosing.

<a id="background"></a>
## Background

It's no secret that I have what some might call an 'unhealthy' obsession with the tracking the snow that may or may not be headed our way. For years, one of my favorite tools for this was an awesome app (that disappeared years ago) called [FreshyMap](https://en.wikipedia.org/wiki/FreshyMap).

{% include figure_link.html url="https://upload.wikimedia.org/wikipedia/en/3/3f/FreshyMapshot.jpg" href="https://en.wikipedia.org/wiki/FreshyMap" caption="Screenshot of a FreshyMap session Image source: wikipedia.com" width="70%" %}

> So, I sez: "Hey! What better opportunity to improve my skills with Flask, interact with some new APIs, and try out some hot new mapping platforms than to create my own homage to the late, great FreshyMap? 
>
> #### Check out the latest version [here](https://snowscraper.herokuapp.com/).

<a id="overview"></a>
#### Overview
This software does two main things:
1. **Scrapes** weather data on every resort in North America (from the good folks at [Opensnow](https://www.opensnow.com)) and integrate that with data from [Google Maps](https://developers.google.com/console).

1. Provides a highly interactive **visualization** tool using ([Plotly Dash](https://dash.plot.ly/)) that I've dubbed "FreshyFinder", to search the aggregated snowfall data in anticipation of spending your days in that perfect POW.

Since each of these facets deserve a fair amount of time to unpack, I've decided to break this into two posts. In this post, we'll focus on web scraping with [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/).

<a id="web"></a>
## Part 1. Web Scraping with Beautiful Soup
The [documentation](https://www.crummy.com/software/BeautifulSoup/) for Beautiful Soup (BS) describes it as "a Python library designed for quick turnaround projects like screen-scraping."

> BS parses anything you give it, and does the tree traversal stuff for you. You can tell it 
- "Find all the links", or 
- "Find all the links of class externalLink", or 
- "Find all the links whose urls match "foo.com", or 
- "Find the table heading that's got bold text, then give me that text."
>
> **Valuable data that was once locked up in poorly-designed websites is now within your reach.**

<a id="installation"></a>
### Installation
1. You can install Beautiful Soup 4\*  with `pip install beautifulsoup4`.
2. You may also need to install the requests toolkit. If so, use `pip` for that, as well.  
`pip install requests`

\*the latest, as of Jan '19

<a id="scraping"></a>
### Example: Scraping a website
First, let's see how we can collect data from a website such as [opensnow.com](www.opensnow.com).
> Before we begin, we want to develop a 'plan-of-attack' for how we are going to systematically collect the data we are interested in. In our case, we are interested in retrieving info on every ski resort in North America. This website happens to have a page for each state, that contains all of the info we need to then scrape from each resort in that state.
>
> *So*, we need to figure out how to:  
> **A.** iteratively scrape data for *each state*, then  
> **B.** scrape data for *each resort*.

Normally, this sounds like a job that might require an ugly *nested loop*. But with BS, the process it made much easier.


```python
# We start with a list of all of the states and provinces we could possibly scrape
states = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    'Alberta': 'AB',
    'British Columbia': 'BC',
    'Manitoba':  'MB',
    'New Brunswick':  'NB',
    'Newfoundland and Labrador':  'NL',
    'Northwest Territories': 'NT',
    'Nova Scotia':  'NS',
    'Nunavut':  'NU',
    'Ontario':  'ON',
    'Prince Edward Island':  'PE',
    'Quebec':  'QC',
    'Saskatchewan':  'SK',
    'Yukon':  'YT'
}

state_abbrevs = list(states.values())
```


```python
import requests
from bs4 import BeautifulSoup
```

For this example, we'll start with the second state in the list: **Alaska**


```python
# Create URL for the first state's website
base = 'https://opensnow.com'
url = base+'/state/'+state_abbrevs[1]
print(url)
```

    https://opensnow.com/state/AK



```python
# Scrape state website
resp = requests.get(url)
state_soup = BeautifulSoup(resp.text, 'html.parser')
```

#### Finding Tags
In order to find the tags associated with each element in a given page, use the following approach:
1. Right-click on an element you are interested in, then choose Inspect (in Chrome).
2. This will open the Developer Tools and show the HTML used to render the selected page element.

---
Now that we are able to scrape the data for an individual state, we can collect the links to *each resort* in the state and iterate through each of them (in the next step), to end up with the snow forecast for each.

> Now is a good time to explain the difference between `.find()` and `.find_all()`. The latter method scans the entire document looking for matching results, but often you'll only expect to find one result.
>
> There's a great example in the [docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find), which illustrates this further.

Using `.find_all()`, we can expect to get back all of the matches (resorts, in this case) present on a given state's page (even if there is only one, as is sometimes the case).


```python
# Select page region to use
big_column = state_soup.find(class_='col-lg-8')

# Get state name
state_name = state_soup.find('h1', {'class': 'title'}).get_text()
print("Scraping 'State name': {}".format(state_name))

# Get resort name(s)
resorts_scrape = big_column.find_all('div', {'class': 'title-location'})
resorts = [resort.getText() for resort in resorts_scrape]
print("Scraping 'Resorts': {}".format(resorts))

# Scrape the table data
table_scrape = big_column.find_all('table', {'class': 'tiny-graph'})
    
# Get forecast for each resort
forecasts = []
for table in table_scrape:
    daily_snow = table.find_all('span')
    forecast_n = [val['value'] for val in daily_snow if val.has_attr('value')]
    forecasts.append(forecast_n)

print("Scraping 'Forecasts': {}".format(forecasts))
```

    Scraping 'State name': Alaska
    Scraping 'Resorts': ['Alyeska', 'Eaglecrest', 'Majestic Heli Ski']
    Scraping 'Forecasts': [['0"', '0"', '0"', '0"', '0"', '0"', '0"', '0-1"', '0"', '1-2"'], ['8"'], ['0-1"', '0-1"', '1-3"', '0-1"', '1-2"', '1-2"', '1-2"', '0"', '0"', '0"'], ['N/A'], ['4-6"', '0-1"', '1-3"', '3-7"', '4-8"', '0-1"', '0"', '0-1"', '0"', '0-1"'], ['N/A']]


**Now we're in business!** Notice the correspondence between the forecast we see in the screenshot below and the data that we scraped? We've still got a bit of cleaning to do, but the data is in our hands!

{% include figure_link.html url="../assets/images/web_scraping/scrape_example.png" href="https://www.opensnow.com" caption="Screenshot of OpenSnow.com" width="60%" %}

> To **re-cap**, we currently have:
> - the name of each state
> - the name of each resort in each state
> - the forecast at each resort
Looks like we are ready to move on to the next phase: using **google-maps** to collect location data for each resort we have scrapped.

<a id="google"></a>
## Part 2. Location Data with Google Maps API

For this section, we'll use a [Python client library](https://github.com/googlemaps/google-maps-services-python) for Google Maps API Web Services to look-up the lat. and long. of each resort. This tool brings together multiple Google utilities including [directions](https://developers.google.com/maps/documentation/directions/), [distances](https://developers.google.com/maps/documentation/distancematrix/), [geocoding](https://developers.google.com/maps/documentation/geocoding/), [elevation](https://developers.google.com/maps/documentation/elevation/), and [more](https://developers.google.com/places/) and makes them available to your Python app. 
> To install:  `pip install -U googlemaps`

<a id="key"></a>
### API Key

Like most modern API's- each Google Maps request **requires an API key** to ID each client. API keys are freely available to anyone with a Google account at https://developers.google.com/console. The type of API key you need is a 'Server key'.


```python
# Import API key
import secrets

# Specify request
url= 'https://maps.googleapis.com/maps/api/geocode/json?'
params = {'address': ('Alyeska'+' '+state_name),
                        'key':secrets.google_places_key,}
print('Request parameters:\n', params, '\n')
req = requests.Request(method = 'GET', url = url,
                        params = sorted(params.items()))                     
prepped = req.prepare()

# Collect response
response = requests.Session().send(prepped)
print('Request response:\n', response.text, '\n')
```

    Request parameters:
     {'address': 'Alyeska Alaska', 'key': 'AIzaSyC9rMVIW9RlR5KT8xaWDhNQY06FlXK6ErE'} 
    
    Request response:
     {
       "results" : [
          {
             "address_components" : [
                {
                   "long_name" : "Alyeska",
                   "short_name" : "Alyeska",
                   "types" : [ "locality", "political" ]
                },
                {
                   "long_name" : "Anchorage",
                   "short_name" : "Anchorage",
                   "types" : [ "administrative_area_level_2", "political" ]
                },
                {
                   "long_name" : "Alaska",
                   "short_name" : "AK",
                   "types" : [ "administrative_area_level_1", "political" ]
                },
                {
                   "long_name" : "United States",
                   "short_name" : "US",
                   "types" : [ "country", "political" ]
                },
                {
                   "long_name" : "99587",
                   "short_name" : "99587",
                   "types" : [ "postal_code" ]
                }
             ],
             "formatted_address" : "Alyeska, AK 99587, USA",
             "geometry" : {
                "location" : {
                   "lat" : 60.96083,
                   "lng" : -149.11083
                },
                "location_type" : "APPROXIMATE",
                "viewport" : {
                   "northeast" : {
                      "lat" : 60.96624569999999,
                      "lng" : -149.0948226
                   },
                   "southwest" : {
                      "lat" : 60.9554134,
                      "lng" : -149.1268374
                   }
                }
             },
             "place_id" : "ChIJBwUV8DJ7yFYRQMXC80-UZ0U",
             "types" : [ "locality", "political" ]
          }
       ],
       "status" : "OK"
    }


**Look at all that data!** And because it's backed up by Google's super-powerful search engine, it's even *robust to minor errors*. 
- Give it a spin! See what it can do.
> Notice, when we change the search parameters from 'Alyeska Alaska' to 'Alyesk Alaska', it still works!

<a id="summary"></a>
### Summary
- In this lesson, we used the Beautiful Soup library to locate elements on a website then scrape their text.
- We also learned how to use an API to access many of Google's powerful geo-location utilities.

<a id="study"></a>
#### Further Study
- Al Sweigart, "[Automating Your Browser and Desktop Apps](https://www.youtube.com/watch?v=dZLyfbSQPXI)" (Quick survey of tools)
- Asheesh Laroia, "[Web scraping: Reliably and efficiently pull data from pages that don't expect it
](https://www.youtube.com/watch?v=52wxGESwQSA)" (In-depth, hands-on tutorial)
- Data Science Dojo, "[Intro to Web Scraping with Python and Beautiful Soup](https://www.youtube.com/watch?v=XQgXKtPSzUI)" (Quick and dirty demo)
