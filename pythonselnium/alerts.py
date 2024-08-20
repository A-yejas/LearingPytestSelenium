import time
from selenium import webdriver
from selenium.webdriver.common.by import By
name = "Rahul"
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
time.sleep(3)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
time.sleep(3)
alertText = alert.text
print(alertText)
time.sleep(3)
assert name in alertText
alert.accept()
