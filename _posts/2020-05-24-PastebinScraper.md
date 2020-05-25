---
layout: post
title: Pastebin scraper
subtitle: Python 3 Script
gh-repo: fancy-sauce/fancy-sauce.github.io
gh-badge: [star, follow]
tags: [script]
comments: true
---
# A simple script to scrape pastebin at random intervals to not get banned

Check [here] before using this script, there may have been an update (https://raw.githubusercontent.com/fancy-sauce/fancy-sauce.github.io/master/pastebinScraper.py)


```
## importing bs4, requests, fake_useragent and csv modules
import bs4, requests, random, time, csv, string
from fake_useragent import UserAgent
from random import randint
from time import sleep

def random_string(stringLength=8):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))

urls = str("https://pastebin.com/raw/" + random_string(8))
print("Initializing url list")
# initialize urllist container list
urllist = []

# generate a certain amount of urls
print("Creating url list")
for i in range(0,50):
    urllist.append(urls)
#        print(urllist)

## initializing the UserAgent object
user_agent = UserAgent()

print("Starting...")
## starting the loop
for url in urllist:

    ## getting the reponse from the page using get method of requests module
    print("Loading fake user agent")
    page = requests.get(url, headers={"user-agent": user_agent.chrome})
    print("Sleeping random interval")
    sleep(randint(1,30))

## storing the content of the page in a variable
    html = page.content

## creating BeautifulSoup object
    soup = bs4.BeautifulSoup(html, "html.parser")
    title = str(soup.find('title'))
    print(title)
    if title != "<title>Pastebin.com - Page Removed</title>":
        goodpage= soup.prettify()
        f = open("Page.txt", "a")
        f.write(goodpage)
        f.close()
        print("Wrote new page to file")
```
