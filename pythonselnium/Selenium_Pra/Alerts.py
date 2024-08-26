from selenium.webdriver.common.alert import Alert
from selenium import webdriver
# Alerts:-
# Accepting / Dismissing alert prompts:
driver = webdriver.Chrome()
Alert(driver).accept()
Alert(driver).dismiss()
# ---
# Inputting a value into an alert prompt:

name_prompt = Alert(driver)
name_prompt.send_keys("Willian Shakesphere")
name_prompt.accept()
# Reading a the text of a prompt for verification:

alert_text = Alert(driver).text
# self.assertEqual("Do you wish to quit?", alert_text)


# kill()
# Kill the browser.
# 
# This is useful when the browser is stuck.
'''
find_element(by='id', value: str | None = None) → WebElement
Find an element given a By strategy and locator.
----
find_elements(by='id', value: str | None = None) → List[WebElement]
Find elements given a By strategy and locator.
Ex:-
elements = driver.find_elements(By.CLASS_NAME, 'foo')
----
get_window_position(windowHandle='current') → dict
Gets the x,y position of the current window.
Usage:
driver.get_window_position()
-------------
get_window_size(windowHandle: str = 'current') → dict
Gets the width and height of the current window.
Usage:
driver.get_window_size()
--------------
implicitly_wait(time_to_wait: float) 
---
set_page_load_timeout(time_to_wait: float) → None
Set the amount of time to wait for a page load to complete before throwing an error.
Args:
time_to_wait: The amount of time to wait
Usage:
driver.set_page_load_timeout(30)
-------
set_script_timeout(time_to_wait: float) → None
Set the amount of time that the script should wait during an execute_async_script call before throwing an error.

Args:
time_to_wait: The amount of time to wait (in seconds)
Usage:
driver.set_script_timeout(30)
'''
