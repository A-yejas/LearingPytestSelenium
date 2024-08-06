from selenium import webdriver
from selenium.webdriver.common.by import By

'''
previously we have a slice method to take the copy.
But in the latest version of Python, there is another method given called copy which is more faster
than slice to create another new list copy from the original list.
'''
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
apnd = []
driver.find_element(By.XPATH,"//span[text()='Veg/fruit name']").click()
veg_tables = driver.find_elements(By.XPATH, "//tr/td[1]")
for veg in veg_tables:
    apnd.append(veg.text)
original_browserlist=apnd.copy()
apnd.sort()
assert  apnd == original_browserlist

