import time

from selenium import webdriver
from selenium.webdriver.common.by import By

'''
previously we have a slice method to take the copy.
But in the latest version of Python, there is another method given called copy which is more faster
than slice to create another new list copy from the original list.
'''
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver=webdriver.Chrome(executable_path=chrome_driver_path,options=options)
driver.get("https://www.google.com")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
apnd = []
time.sleep(4)
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
veg_tables = driver.find_elements(By.XPATH, "//tr/td[1]")
time.sleep(6)
for veg in veg_tables:
    apnd.append(veg.text)
original_browserlist=apnd.copy()
apnd.sort()
assert  apnd == original_browserlist
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>')
time.sleep(8)
