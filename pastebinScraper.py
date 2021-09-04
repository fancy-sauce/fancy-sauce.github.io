import bs4, requests, random, time, string
#from fake_useragent import UserAgent
from random import randint
from time import sleep

def random_string(stringLength=8):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))

#urls = str("https://pastebin.com/raw/" + random_string(8))
print("Initializing url list")
# initialize urllist
urllist = []

print("Creating url list")
for i in range(0,50):
    urls = str("https://pastebin.com/raw/" + random_string(8))
    urllist.append(urls)
    print(urllist)

## initializing the UserAgent object
#user_agent = UserAgent()

print("Starting...")
## starting the loop
for url in urllist:

    ## getting the reponse from the page using get method of requests module
    #print("Loading fake user agent")
    page = requests.get(url, headers={"user-agent": "chrome"})
    #print("Sleeping random interval")
    sleep(randint(1,5))
    print(url)

## storing the content of the page in a variable
    html = page.content

## creating BeautifulSoup object
    soup = bs4.BeautifulSoup(html, "html.parser")
    title = str(soup.find('title'))
    #print(title)
    if title != "<title>Pastebin.com - Page Removed</title>" and title != "<title>Pastebin.com - Not Found (#404)</title>":
        goodpage= soup.prettify()
        f = open('scrapedpages.txt', "a")
        f.write(goodpage)
        f.close()
        print("Wrote new page to file")
