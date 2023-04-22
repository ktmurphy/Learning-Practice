"""
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()
browser.get('https://inventwithpython.com')
try:
    elem = browser.find_element(By.CLASS_NAME, 'card-img-top')
    print(elem)
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name')



from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()
browser.get('https://inventwithpython.com')
linkElem = browser.find_element(By.LINK_TEXT,'Read Online for Free')
print(type(linkElem))
linkElem.click()
"""
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Firefox()
browser.get('https://login.metafilter.com')
userElem = browser.find_element(By.ID, 'user_name')
userElem.send_keys('username')

passwordElem = browser.find_element(By.ID, 'user_pass')
passwordElem.send_keys('password')
#passwordElem.submit()
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get("https://nostartch.com")
htmlElem = browser.find_element(By.TAG_NAME, "html")
htmlElem.send_keys(Keys.END)
# htmlElem.send_keys(Keys.HOME)
