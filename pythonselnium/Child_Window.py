import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver import Firefox
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.implicitly_wait(8)
driver.find_element(By.LINK_TEXT, "Click Here").click()
OpenchildWindow=driver.window_handles
'''
# "driver.window_handles" this property will get the window names of all the windows which are open.
# what does this window handle's property does this it will grab all the windows which got open and ' \
#it will put in the list. the order in which your automation opens the browser.
In that order it will get stored in the list.
'''
driver.switch_to.window(OpenchildWindow[1])
print(driver.find_element(By.TAG_NAME, "h3").text)
driver.switch_to.window(OpenchildWindow[0])
assert "Opening a new window"== driver.find_element(By.TAG_NAME, "h3").text

driver.quit()
##Assigment

