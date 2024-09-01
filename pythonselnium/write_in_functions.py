# import time
#
'''
Synchronized means only one thread acting upon a object so execution wise or performance is very slow..
.Unsynchronized  means multipel threads are acting upon a object so execution wise or performance wise very fast

'''
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
#
# def test_01_actions():
#     driver = webdriver.Chrome()
#     driver.get("https://awesomeqa.com/practice.html")
#
#     first_name = driver.find_element(By.XPATH,"//input[@name='firstname']")
#     # Shirt Down + types + Shift Up
#     actions = ActionChains(driver)
#     actions.key_down(Keys.SHIFT).send_keys_to_element(first_name,"the testing academy").key_up(Keys.SHIFT).context_click().perform()
#
#
#
#     time.sleep(10)
#     driver.quit()
import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# def test_actions():
#     driver = webdriver.Chrome()
#     driver.get("https://the-internet.herokuapp.com/windows")
#     driver.maximize_window()
#     # Windows
#     parent_window = driver.current_window_handle
#
#     print(parent_window)
#
#     link = driver.find_element(By.LINK_TEXT, "Click Here")
#     link.click()
#
#     window_handles = driver.window_handles # 2
#     print(window_handles)
#
#
#     for handle in window_handles:
#         driver.switch_to.window(handle) # child
#         if "New Window" in driver.page_source:
#             print("Testcase Passed, Switched to Child Window")
#             break
#
#     time.sleep(3)
#     driver.switch_to.window(parent_window)
#     time.sleep(5)
'''
 A stack overflow can occur in Python when a function recursively calls itself without a proper exit condition, 
 causing the number of function calls on the call stack to grow indefinitely and eventually overflow.
 import sys
print(sys.setrecursionlimit(10**6))
##########
def infinite():
    while True:
        infinite()

infinite()
Ans:- RecursionError: maximum recursion depth exceeded
################
finalize provides a straight forward way to register a cleanup function to be called when an object is 
garbage collected.
'''

# Search in Chatgpt  create button not clickable exception call in python selenium And Single also search in gpt
#test90pop12java99pyt , out - tset90pop12avaj99typ
import re

def reverse_alphabets(input_string):
    # Find all alphabetic characters using regex
    alphabets = re.findall(r'[a-zA-Z]', input_string)

    # Reverse the list of alphabetic characters
    alphabets.reverse()

    # Initialize an index to track the position in the reversed alphabets
    alpha_index = 0

    # Create a new list to hold the result
    result = []

    # Loop through the original string
    for char in input_string:
        # If the character is alphabetic, replace it with the reversed alphabetic character
        if char.isalpha():
            result.append(alphabets[alpha_index])
            alpha_index += 1
        else:
            # If it's not alphabetic, just keep the original character
            result.append(char)

    # Join the list into a string and return
    return ''.join(result)

# Example input
input_string = "test90pop12java99pyt$$@#"

# Get the output
output = reverse_alphabets(input_string)

print(output)
##############
def compress_string(input_str):
    # Initialize variables
    compressed = []
    count = 1

    # Iterate through the string
    for i in range(1, len(input_str)):
        if input_str[i] == input_str[i - 1]:
            count += 1  # Increment count if current char is the same as the previous
        else:
            compressed.append(input_str[i - 1] + str(count))  # Append the character and count
            count = 1  # Reset count for new character

    # Append the last character and its count
    compressed.append(input_str[-1] + str(count))

    # Join the list into a compressed string
    return ''.join(compressed)

# Example input
str_input = 'aaaabbbbbccc'

# Get the compressed output
output = compress_string(str_input)

print(output)
print(0.1+0.4)
