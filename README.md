# web-scraper

This is a webscraper made in python that beeps when specified text is found on a specified URL page source. It will then open a pop up tab in your computer's default browser. It is quite slow on large pages. I made this in an attempt to purchase an Nvidia RTX 3080 on release without resorting to using a checkout bot as I feel those are simply unfair. I am happy to say it worked like a charm.



Usage:
=====

WebScraper.py [-h] [--headless] [-c] [-p] {chrome,firefox}

positional arguments:

  {chrome,firefox}    *Browser to scrape with*
  
optional arguments:

  -h, --help          *show this help message and exit*
  
  --headless          *Enable headless browser mode*
  
  -c, --continuous    *Script will continue to run even after match is found*
  
  -p, --disablepopup  *Do not open URL in default browser when match is found*




Requirements:
=====

**Modules:**
* playsound
* selenium

**Others:**
* gecko driver to scrape with firefox
* chromedriver to scrape with chrome

Currently chrome and firefox are the only browsers supported. Others should be implemented in the future.



Todo:
=====
* implement other browsers
* implement a setup.py file
* rewrite in C++
