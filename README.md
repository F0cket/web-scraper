
# Web-Scraper

## Overview
Web-Scraper is a simple Python-based webscraper that beeps when user-specified text is found on a designated URL page source. Following the beep, Web-Scraper will then open a pop-up tab in your computer's default browser. It can be used for a wide range of activities, from checking if a product is back in stock to auto-fetching prices.

Please note that Web-Scraper runs slower on larger pages.


## Requirements

* Python 3.0
* Chrome or Firefox web-browser

**Python Modules:**
* playsound
* selenium

**Browser-Specific Drivers:**
* Gecko driver to scrape with Firefox
* Chromedriver to scrape with Chrome

Currently, Chrome and Firefox are the only browsers supported. Support for more browsers will be added in later builds.


## Installation
Install from the source file:

```pip install -r requirements.txt```

## How to Use

```WebScraper.py [-h] [--headless] [-c] [-p] {chrome,firefox}```

Once the script is entered, the console will prompt the user to enter the text they wish to scrape for.

**Positional Arguments:**

  `{chrome,firefox}`    Browser to scrape with
  
**Optional Arguments:**
| Argument| Description |
|--|--|
|`-h`, `--help`     |  Show this help message and exit |
|`--headless`  |Enable headless browser mode|
| `-c`, `--continuous` |Script will continue to run even after match is found|
|`-p`, `--disablepopup`|Will not open URL in default browser when match is found|




## Future Releases
Future builds will implement support for additional web-browsers and switch to C++.


