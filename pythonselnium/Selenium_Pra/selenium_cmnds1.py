import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.relative_locator import locate_with
driver =webdriver.Chrome()
# driver = webdriver.Firefox()
# driver.implicitly_wait(10)
# driver.get("http://www.python.org")
#
# assert "Python" in driver.title
#
# time.sleep(5)
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# time.sleep(5)
# elem.send_keys("pycon")
# time.sleep(1)
# elem.send_keys(Keys.ENTER)
#
# # print(s)
# time.sleep(4)
# assert "No results found." not in driver.page_source
# driver.close()
# # time.sleep(3)
# ----------------
# driver=webdriver.Chrome()
# driver.maximize_window()
# driver.get('https://tdp--qa--pathfinder-hcl.edgenetworks.ai/auth/login')
# time.sleep(3)
# driver.find_element(By.XPATH,"//input[@data-attr-auth-login-username='login-username']").send_keys('ramesh.vengatachalam@hcl.com')
# time.sleep(2)
# driver.find_element(By.XPATH,"//input[@data-attr-auth-login-username='login-password']").send_keys('51350200')
# # ele = driver.find_element(By.XPATH,"//input[@data-attr-auth-login-username='login-password']").send_keys('51350200')
# # driver.find_element(By.XPATH,"//button[@data-attr-auth-login-btn='login-btn']")
# time.sleep(3)
# print(">>>>>>>>>>>>>>>>>>")
# driver.find_element(By.XPATH,"//button[@data-attr-auth-login-btn='login-btn']").send_keys(Keys.ENTER)
# time.sleep(10)
# driver.find_element(By.XPATH,"//span[text()='How would you describe the job you do right now to your friends?']").click()
# skill=driver.find_element(By.XPATH,"//input[@placeholder='Search for titles']")
# time.sleep(10)
# opt=skill.send_keys('java', Keys.ARROW_DOWN)
#
# time.sleep(15)
# print(opt)
######

'''
#get_attribute ():-
element = driver.find_element(By.XPATH, "//select[@name='name']")
all_options = element.find_elements(By.TAG_NAME, "option")
for option in all_options:
    print("Value is: %s" % option.get_attribute("value"))
    option.click()
------
This will find the first “SELECT” element on the page, and cycle through each of its OPTIONs in turn, 
printing out their values, and selecting each in turn.

As you can see, this isn’t the most efficient way of dealing with SELECT elements. 
WebDriver’s support classes include one called a “Select”, which provides useful methods for interacting with these:
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element(By.NAME, 'name'))
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)
##WebDriver also provides features for deselecting all the selected options:
select = Select(driver.find_element(By.ID, 'id'))
select.deselect_all()
--
Suppose in a test, we need the list of all default selected options, 
Select class provides a property method that returns a list.
select = Select(driver.find_element(By.XPATH, "//select[@name='name']"))
all_selected_options = select.all_selected_options
--To get all available options:
options = select.options
----from selenium.webdriver import ActionChains
action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()
'''
'''
 Cookies
Before moving to the next section of the tutorial, you may be interested in understanding how to use cookies. 
First of all, you need to be on the domain that the cookie will be valid for:
---The heading (h1) element can be located like this:
example:- heading1 = driver.find_element(By.TAG_NAME, 'h1')
'''
# driver.get("https://tdp--qa--pathfinder-hcl.edgenetworks.ai/auth/login")
#
# # Now set the cookie. This one's valid for the entire domain
# cookie = {'name' : 'foo', 'value' : 'bar'}
# driver.add_cookie(cookie)
# time.sleep(5)
# # And now output all the available cookies for the current URL
# coo=driver.get_cookies()
# print(coo)
'''
#Exceptions:- 
selenium.common.exceptions.ElementNotInteractableException
#Thrown when an element is present in the DOM but interactions with that element will hit another element due to paint order.
ElementNotSelectableException :- Thrown when trying to select an unselectable element.
ElementNotVisibleException:- Thrown when an element is present on the DOM, but it is not visible, and so is not able to be interacted with.
InvalidArgumentException:-The arguments passed to a command are either invalid or malformed.
InvalidElementStateException:- Thrown when a command could not be completed because the element is in an invalid state.
This can be caused by attempting to clear an element that isn’t both editable and resettable.
NoAlertPresentException:- Thrown when switching to no presented alert.
This can be caused by calling an operation on the Alert() class when an alert is not yet on the screen.
NoSuchAttributeException :- hrown when the attribute of element could not be found.
You may want to check if the attribute exists in the particular browser you are testing against. 
Some browsers may have different property names for the same property. (IE8’s .innerText vs. Firefox .textContent)
NoSuchElementException:- Thrown when element could not be found.
NoSuchWindowException:- Thrown when window target to be switched doesn’t exist.
To find the current set of active window handles, you can get a list of the active window handles in the following way:
StaleElementReferenceException:- Thrown when a reference to an element is now “stale”.
Stale means the element no longer appears on the DOM of the page.
TimeoutException:- Thrown when a command does not complete in enough time.
UnexpectedAlertPresentException :- Thrown when an unexpected alert has appeared.
'''
# ActionChanins:-
'''
selenium.webdriver.common.action_chains.ActionChains
1.ActionChains are a way to automate low level interactions such as mouse movements, 
mouse button actions, key press, and context menu interactions.
2.This is useful for doing more complex actions like hover over and drag and drop.
Genaret Action:-
1.When you call methods for actions on the ActionChains object, 
the actions are stored in a queue in the ActionChains object.
2.When you call perform(), the events are fired in the order they are queued up.
ActionChains can be used in a chain pattern:
menu = driver.find_element(By.CSS_SELECTOR, ".nav")
hidden_submenu = driver.find_element(By.CSS_SELECTOR, ".nav #submenu1")
ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()
OR actions can be queued up one by one, then performed.:
menu = driver.find_element(By.CSS_SELECTOR, ".nav")
hidden_submenu = driver.find_element(By.CSS_SELECTOR, ".nav #submenu1")

actions = ActionChains(driver)
actions.move_to_element(menu)
actions.click(hidden_submenu)
actions.perform()
Either way, the actions are performed in the order they are called, one after another.
----------------
click(on_element: WebElement | None = None)
click_and_hold(on_element: WebElement | None = None):- Holds down the left mouse button on an element.
context_click(on_element: WebElement | None = None) :-Performs a context-click (right click) on an element.




'''
