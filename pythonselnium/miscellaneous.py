import time
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
'''
That's how you are integrating your requirements to your browser before invocation.
you will not see any browser opening.
You see, no browser is running mode, but you will see very soon.
You see that process finished without even opening the browser.
The process got finished.
How?
It's because you ask to run in headless mode.
So by default chrome opens in head mode, but you can also suppress to run that in headless.
So similarly, there are other options.
'''
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors") #ignore all the certification errors

driver = webdriver.Chrome(options=chrome_options) #So if you don't put it here, then when it invoking your browser will
# / not have any clue about running
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(2)
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
print("Script is done")
