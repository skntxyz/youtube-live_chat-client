import time
import os
from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
import collections
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)


browser = webdriver.Firefox()
browser.get(raw_input("enter url to live stream:"))

ui.WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "comment-text")))
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
        user = li.find_next("span", {"class":"author"})
        user = user.find_next("a").text
        user = unicode(user).lstrip().replace('\n','')
        usertext = "".join(user)

        comment = li.find("div", {"class":"comment-text"})
        comment = unicode(comment.text).lstrip().replace('\n','')
        commenttext = "".join(comment)
        
        if (usertext + ": " + commenttext) not in comments:
            comments.append(usertext + ": " + commenttext)
            print usertext + ": " + commenttext


#while True:
#    os.system(['clear','cls'][os.name == 'nt'])
#    resp = urllib2.urlopen("http://www.youtube.com/user/AratorYT/live")
#    src = resp.read()

#    soup = BeautifulSoup(src)
#    comments = soup.find_all("div", {"class":"comment-text"})
#    print comments
#    for comment in comments:
#        print comment
#    time.sleep(2)
    
