import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
check=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
for checks in check:
    if checks.get_attribute('value')=="option2":
        checks.click()
        assert checks.is_selected()
        # time.sleep(2)
        break
radio = driver.find_elements(By.CSS_SELECTOR, '.radioButton')
# time.sleep(2)
radio[2].click()
assert radio[2].is_selected()
displaybox = driver.find_element(By.ID,"displayed-text").is_displayed()
assert displaybox
Hide = driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()

