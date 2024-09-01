import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with



# name = "Rahul"
# driver = webdriver.Chrome()
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# time.sleep(3)
# driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name)
# time.sleep(3)
# driver.find_element(By.ID, "alertbtn").click()
# alert = driver.switch_to.alert
# time.sleep(3)
# alertText = alert.text
# print(alertText)
# time.sleep(3)
# assert name in alertText
# alert.accept()
# -----------------------------

name = "Rahul"
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
time.sleep(3)

alert_button = driver.find_element(By.ID, "alertbtn")
input_option=driver.find_element(locate_with(By.CSS_SELECTOR, "#name").above(alert_button))
input_option.send_keys(name)
time.sleep(3)
# driver.execute_script("window.scrollTo(0,600)")
time.sleep(3)
# hide_button=driver.find_element(locate_with(By.ID,'hide-textbox').below(alert_button)).click()
# confirm_button=driver.find_element(locate_with(By.ID,'confirmbtn').to_right_of(alert_button))
# confirm_button.click()
# alert = driver.switch_to.alert
time.sleep(3)
# alertText = alert.text
# print(alertText)
time.sleep(3)
# alert.accept()

open_window_button=driver.find_element(locate_with(By.ID, 'opentab').to_left_of(alert_button)).click()
time.sleep(3)
OpenchildWindow=driver.window_handles
driver.switch_to.window(OpenchildWindow[1])
print(">>>>>>>>>>>>>>>>>>>")
time.sleep(3)
driver.switch_to.window(OpenchildWindow[0])
time.sleep(3)

# assert name in alertText
# alert.accept()
