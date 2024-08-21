import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
'''
actions = context_click() >> Means rigt Click
actions.click_and_hold()  >> long hold
actions.double_click()  >> Double click
actions.drag_and_drop()  >> Drag and drop
But one thing you need to remember whenever you perform any method using actions object at the end you
want to eliminate with the method called perform.
Then only this action will get activated.
So even you can do double click context, click, drag and drop, click and hold whatever methods you.
perform for all these actions at the end, you have to write like this thought perform.
Then only the sequence of actions will get executed.

'''


driver = webdriver.Chrome() #So if you don't put it here, then when it invoking your browser will not have any clue about running
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
# driver.manage().window().maximize()
driver.implicitly_wait(2)
actions = ActionChains(driver)
# driver.manage().window().maximize()
# driver.execute_script("window.scrollTo(0, 800)")
actions.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")#Sroll the screen
time.sleep(3)
print("Execution is done")
# actions.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()

# actions.context_click(driver.find_element(By.LINK_TEXT, "Reload").click()).perform()
# time.sleep(2)

