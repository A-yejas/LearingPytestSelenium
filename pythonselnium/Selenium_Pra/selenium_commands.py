'''
title = driver.title  #You can read the current page title from the browser:
url = driver.current_url  # You can read the current URL from the browser’s address bar using:
'''
import time

#Implicit waits
'''
***driver.implicitly_wait(2)
1.Selenium has a built-in way to automatically wait for elements called an implicit wait
2.This is a global setting that applies to every element location call for the entire session. 
3.the default value is 0, which means that if the element is not found, it will immediately return an error.
4.If an implicit wait is set, the driver will wait for the duration of the provided value before returning the error.
5.Note that as soon as the element is located, the driver will return the element reference and the code will 
continue executing, so a larger implicit wait value won’t necessarily increase the duration of the session
'''
#Explicit waits
'''
Example:- 
from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.ID, 'someid'))).
1.Explicit waits are like pauses in the code that check repeatedly if a certain condition is met before moving on.
2.For example,if you're waiting for a button to appear on the page, the code will keep checking until the button 
showsup.
3.If the button doesn't appear within a set time (say, 10 seconds), the code will stop and throw an error.
4.The good thing about explicit waits is that you can define exactly what you're waiting for 
(e.g., a button to appear, a message to be visible, etc.).
5.Selenium’s Wait class makes it easier by automatically waiting for the element to be present 
without you having to add extra checks. (OR) 
Another nice feature is that, by default, the Selenium Wait class automatically waits for 
the designated element to exist.
--------------------------------------------
Expected Conditions:- 
title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present
------------------
#Customization:-
The Wait class can be instantiated with various parameters that will change how the conditions are evaluated.

This can include:
**Changing how often the code is evaluated (polling interval)
**Specifying which exceptions should be handled automatically
**Changing the total timeout length
**Customizing the timeout message
****For instance, if the element not interactable error is retried by default, 
then we can add an action on a method inside the code getting executed 
(we just need to make sure that the code returns true when it is successful):

    errors = [NoSuchElementException, ElementNotInteractableException]
    wait = WebDriverWait(driver, timeout=2, poll_frequency=.2, ignored_exceptions=errors)
    wait.until(lambda d : revealed.send_keys("Displayed") or True)

'''
#File Upload
'''
    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    file_input.send_keys(upload_file)
    driver.find_element(By.ID, "file-submit").click()
'''
#Relative Locators
'''
# navigate to this path easily to understand
1.Above:- 
If the email text field element is not easily identifiable for some reason, but the password text field element is, 
we can locate the text field element using the fact that it is an “input” element “above” the password element.
###email_locator = locate_with(By.TAG_NAME, "input").above({By.ID: "password"})
2.Below:-
If the password text field element is not easily identifiable for some reason, but the email text field element is, 
we can locate the text field element using the fact that it is an “input” element “below” the email element.
###password_locator = locate_with(By.TAG_NAME, "input").below({By.ID: "email"})
3.Left of:-
If the cancel button is not easily identifiable for some reason, but the submit button element is, we can locate 
the cancel button element using the fact that it is a “button” element to the “left of” the submit element.
###cancel_locator = locate_with(By.TAG_NAME, "button").to_left_of({By.ID: "submit"})
4.Right of:-
If the submit button is not easily identifiable for some reason, but the cancel button element is, we can locate 
the submit button element using the fact that it is a “button” element “to the right of” the cancel element.
### submit_locator = locate_with(By.TAG_NAME, "button").to_right_of({By.ID: "cancel"})
5.Near:-
If the relative positioning is not obvious, or it varies based on window size, you can use the near method to identify 
an element that is at most 50px away from the provided locator.
##email_locator = locate_with(By.TAG_NAME, "input").near({By.ID: "lbl-email"})
6.Chaining relative locators:-
You can also chain locators if needed. Sometimes the element is most easily identified as being both above/below one 
element and right/left of another
## submit_locator = locate_with(By.TAG_NAME, "button").below({By.ID: "email"}).to_right_of({By.ID: "cancel"})
Pause:-
Pointer movements and Wheel scrolling allow the user to set a duration for the action, but sometimes you just need to 
wait a beat between actions for things to work correctly.
Example:- 
    clickable = driver.find_element(By.ID, "clickable")
    ActionChains(driver)\
        .move_to_element(clickable)\
        .pause(1)\
        .click_and_hold()\
        .pause(1)\
        .send_keys("abc")\
        .perform()
8.Release All Actions:-
There is a special method to release all currently depressed keys and pointer buttons. This method is 
implemented differently in each of the languages because it does not get executed with the perform method.
##    ActionBuilder(driver).clear_actions()
'''
# There are only 5 basic commands that can be executed on an element:

# click (applies to any element)
# send keys (only applies to text fields and content editable elements)
# clear (only applies to text fields and content editable elements)
# submit (only applies to form elements)
# select (see Select List Elements)
'''
1.Is Displayed:- 
This method is used to check if the connected Element is displayed on a webpage. Returns a Boolean value, 
True if the connected element is displayed in the current browsing context else returns false.
# Navigate to the url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

# Get boolean value for is element display
is_email_visible = driver.find_element(By.NAME, "email_input").is_displayed()
---
2.Is Enabled:-
This method is used to check if the connected Element is enabled or disabled on a webpage. Returns a boolean value, 
True if the connected element is enabled in the current browsing context else returns false.
Example:- 
    # Navigate to url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

    # Returns true if element is enabled else returns false
value = driver.find_element(By.NAME, 'button_input').is_enabled()
3.Is Selected:-
This method determines if the referenced Element is Selected or not. 
This method is widely used on Check boxes, radio buttons, input elements, and option elements.
Example:- 
    # Navigate to url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

    # Returns true if element is checked else returns false
value = driver.find_element(By.NAME, "checkbox_input").is_selected()
4.Tag Name :- 
It is used to fetch the TagName of the referenced Element which has the focus in the current browsing context.
Example:-
    # Navigate to url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

    # Returns TagName of the element
attr = driver.find_element(By.NAME, "email_input").tag_name
5. **Size and Position:**-
It is used to fetch the dimensions and coordinates of the referenced element.
The fetched data body contain the following details:

X-axis position from the top-left corner of the element
y-axis position from the top-left corner of the element
Height of the element
Width of the element
----------------
Example:- 
from selenium import webdriver
from selenium.webdriver.common.by import By
    # Navigate to url
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(10)
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

time.sleep(10)
    # Returns height, width, x and y coordinates referenced element
res = driver.find_element(By.NAME, "range_input").rect
print(res)
--------------
Get CSS Value:- 
Retrieves the value of specified computed style property of an element in the current browsing context.
Example:-
from selenium import webdriver
from selenium.webdriver.common.by import By
    # Navigate to url
driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(10)
    # Navigate to Url
driver.get('https://www.selenium.dev/selenium/web/colorPage.html')

    # Retrieves the computed style property 'color' of linktext
cssValue = driver.find_element(By.ID, "namedColor").value_of_css_property('background-color')
print(cssValue)
-->Text Content:- Retrieves the rendered text of the specified element.
Example:-
   # Navigate to url
driver.get("https://www.selenium.dev/selenium/web/linked_image.html")

    # Retrieves the text of the element
text = driver.find_element(By.ID, "justanotherlink").text
-->Fetching Attributes or Properties:-
Fetches the run time value associated with a DOM attribute. 
Example:- 
It returns the data associated with the DOM attribute or property of the element.  
# Navigate to the url
driver.get("https://www.selenium.dev/selenium/web/inputs.html")

# Identify the email text box
email_txt = driver.find_element(By.NAME, "email_input")

# Fetch the value property associated with the textbox
value_info = email_txt.get_attribute("value")
  
'''
