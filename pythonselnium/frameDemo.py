import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/iframe")

driver.maximize_window()
driver.implicitly_wait(5)
alert=driver.switch_to.alert
alert.dismiss()
time.sleep(2)
driver.switch_to.frame("mce_0_ifr")
time.sleep(2)

driver.find_element(By.ID,"tinymce").clear()
time.sleep(3)
driver.find_element(By.ID,"tinymce").send_keys("i am unable to automate")
driver.switch_to.default_content() #back to our default page cheomw
print(driver.find_element(By.CSS_SELECTOR,"h3").text)



