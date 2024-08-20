'''
Selenium supports a multiple ways to identify the elements.
ID, XPath, CssSelector, Classname , name, linktext
Class is one of the attribute defined by developer for that edit box.
Select locator something which will always be unique in most of cases
xpath = "//tagname[@attribute='value']
cssselector = tagname[attribute='value'] , #id, .class
i am somehow comfortable with CSS selectors because that's a fast and reliable than any other locator.
##DropDowns:- So let's get started with static.
So to handle static dropdown selenium guys have came up with one class called "Select".
So using that class it is very easy to handle them.
'''
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://Rahulshettyacademy.com/angularpractice/')
test = driver.getCurrentUrl()
print(test)
time.sleep(2)

# b=driver.title
# c=driver.current_url
# print(b)
# print(c)
time.sleep(2)

c=driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
print(c)

time.sleep(2)

driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456'")
driver.find_element(By.ID, "exampleCheck1").click()
time.sleep(2)
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys('rahul')
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
drop_down=Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
# drop_down(Keys.CONTROL, 'a')

time.sleep(2)
drop_down.select_by_index(1)
time.sleep(2)
drop_down.select_by_visible_text('Male')
# drop_down.select_by_value()

driver.find_element(By.XPATH,"//input[@type='submit']").click()
val = driver.find_element(By.CLASS_NAME, "alert-success").text

time.sleep(2)
assert "Success" in val
driver.find_element(By.XPATH,"(//input[@name='name'])[2]").send_keys('HelloAgain')

