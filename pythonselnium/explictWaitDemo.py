'''
Q:-Welcome back.
let's see how to use explicit wait

So problem here is with implicit wait you are actually waiting.
Wherever the element is not displayed, you are waiting for 5 seconds and if it displays before that,
you are continuing.
Right, which is good.
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys('ber')
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count=(len(results))
assert count > 0
#chaining element
#You are chaining your parent web element to child web element to construct dynamically.This concept as chaining of web elements.

for result in results:
    result.find_element(By.XPATH, "div/button").click()



driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

#Sum
prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)
print(sum)
total_amount = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)

assert sum == total_amount



driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
# time.sleep(5)
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)
