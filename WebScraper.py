import time
from selenium import webdriver
from selenium import common
import re
import webbrowser
from playsound import playsound
from playsound import PlaysoundException
import random
import threading
import argparse
import sys

#Args
parser = argparse.ArgumentParser(description = "Auto refreshes a website and plays a sound if specified text is present in the source.")
parser.add_argument("browser", choices=['chrome', 'firefox'], help="Browser to scrape with")
parser.add_argument("--headless",help="Enable headless browser mode", action="store_true")
parser.add_argument("-c", "--continuous", help="Continuous Mode. Script will continue to run even after match is found", action="store_true")
parser.add_argument("-p", "--disablepopup", help="Do not open URL in default browser when match is found", action="store_false")
parser.parse_args()
args = parser.parse_args()

#Establish driver
if args.browser == "chrome":
    try:
        print("Starting Chrome driver.")
        time.sleep(1)
        op = webdriver.ChromeOptions()
        op.add_argument("log-level=3")
        if args.headless:
            print("Headless mode enabled.")
            op.add_argument("headless")
        driver = webdriver.Chrome(options = op)

    except:
        print("Could not start the chrome driver.\n1. Get it here. https://chromedriver.chromium.org/\n2. Ensure it is placed in your operating system's enviornment variables")
        exit()
        
##elif left for future browser additions
elif args.browser == "firefox":
    try:
        print("Starting Gecko driver.")
        time.sleep(1)
        op = webdriver.FirefoxOptions()
        op.add_argument("log-level=3")
        if args.headless:
            print("Headless mode enabled.")
            op.headless = True
        driver = webdriver.Firefox(options = op)
    except:
        print("Could not start the geko driver.\n1. Get it here. https://github.com/mozilla/geckodriver/releases\n2. Ensure it is placed in your operating system's enviornment variables")
        exit()

#Main Method
def scrape(url,text):
    print("Scraping", url, "for", "\"" +text+"\"")
    while True:
        try:
            source = driver.get(url)
            time.sleep(random.randint(1,5))
            if re.search(text, driver.page_source, re.IGNORECASE):
                print("Found", "\"" +text+"\"", "on page.")
                if args.disablepopup:
                    webbrowser.open(url)
                playsound("Beep.mp3")
                if not args.continuous:
                    driver.quit()
                    exit()
            else:
                time.sleep(random.randint(2,5))
                driver.refresh()
        except common.exceptions.WebDriverException:
            print("Error. The driver window was likely manually closed or the URL is not valid.")
            exit()
        except PlaysoundException:
            print("\n\nThe \"Beep.mp3\" file is not in the same directory as the .py file.\n1. Download it from get hub and place it in the same folder as this .py file.\
                    \n2. Move any .mp3 file to this folder and rename it to \"Beep.mp3\"")
            driver.quit()
            exit()

#Start Here    
url = str(input("Enter the url you would like to scrape: "))
text = str(input("Enter the text you wish to search for: "))
threading.Thread(target=scrape, args=(url,text,)).start()

