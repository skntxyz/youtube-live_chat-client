import os
import sys
import time
import collections
# beautifulsoup
from bs4 import BeautifulSoup
# selenium
import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# unicode support
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

# init webdriver
browser = webdriver.Firefox()
browser.get(raw_input("enter url to live stream:"))

# wait for the chat to load
ui.WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "comment-text")))

# get the element with all comments
allcomments = browser.find_element_by_id("all-comments")

# comments
comments = list()
src = allcomments.get_attribute("outerHTML")
soup = BeautifulSoup(src)

# look for new comments
while True:
    src = allcomments.get_attribute("outerHTML")
    soup = BeautifulSoup(src)

    for li in soup.find_all("li"):
		# get the username
        user = li.find_next("span", {"class":"author"})
        user = user.find_next("a").text
        user = unicode(user).lstrip().replace('\n','')
        usertext = "".join(user)

		# get the commenttext
        comment = li.find("div", {"class":"comment-text"})
        comment = unicode(comment.text).lstrip().replace('\n','')
        commenttext = "".join(comment)
        
		# if they dont exist already, print and add them
        if (usertext + ": " + commenttext) not in comments:
            comments.append(usertext + ": " + commenttext)
            print usertext + ": " + commenttext