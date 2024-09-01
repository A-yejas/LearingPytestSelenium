'''
Q:-let's see what is implicit weight.
1.So implicit weight is more like global time.
Out on top of your script, you will declare a global timeout.
So once you declare your driver object here, you will say driver dot implicit wait.
So let's say if it's a 5 seconds, this is your global timeout to the script.
So what does this imply?
It does help here.
Now, if any element is not shown on the page, it will wait a max of 5 seconds for that to show up.
So 5 seconds is the max timeout.
Let's say if that element is just displayed in 2 seconds, then immediately it identifies that and proceeds
so that it will save you the 3 seconds time.
So it's not like it blindly wait for 5 seconds every time when it could not find the object.
So this is the max timeout.
How much time?
It will wait.
But if your objects are displayed in 2 seconds or one second, that's fine.
It will immediately proceed further in your test without being waiting for 5 seconds.
But in case of sleep's problem is if you put 2 seconds, it will slip 2 seconds no matter what.
Even if that element is displayed in one second, it blindly closes its eyes until the timeout is done.
So that means that is not that efficient.
Right?
So whereas an implicit wait, you will set global timeout, but even if it shows up in between, then
it will proceed further in your execution.
And this implicit rate as you are declaring in global it applies to each and every line in your code.
So wherever, if object is not identified, it will wait until that particular time.
Now let's see what happens here.

'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys('ber')
time.sleep(3)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count=(len(results))
assert count > 0
#chaining element
#You are chaining your parent web element to child web element to construct dynamically.This concept as chaining of web elements.

for result in results:
    result.find_element(By.XPATH, "div/button").click()
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
# time.sleep(5)
driver.find_element(By.CLASS_NAME,"promoInfo").click()
# wait=WebDriverWait(driver=self.driver,timeout=5)
#wait.until(EC.alert_is_present())

