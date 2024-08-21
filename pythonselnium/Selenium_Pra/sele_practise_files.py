'''
1.Starting from version 4.6.0 (November 4, 2022) selenium comes with Selenium Manager packed in distribution.
Selenium Manager is a new tool that helps to get a working environment to run Selenium out of the box
2.The unittest module is a built-in Python module based on Java’s JUnit.
This module provides the framework for organizing the test cases.
###from selenium.webdriver.common.keys import Keys
The Keys class provides keys in the keyboard like RETURN, F1, ALT etc.
###from selenium.webdriver.common.by import By
The By class is used to locate elements within a document.
###class PythonOrgSearch(unittest.TestCase):
The test case class is inherited from unittest.TestCase.
Inheriting from the TestCase class is the way to tell unittest module that this is a test case:
***1.Selenium Python bindings provides a simple API to write functional/acceptance tests using Selenium WebDriver.
2.Through Selenium Python API you can access all functionalities of Selenium WebDriver in an intuitive way.
***Drivers:--Selenium requires a driver to interface with the chosen browser.
    1.WebDriver is designed as a simple and more concise programming interface.
    2.WebDriver is a compact object-oriented API.
    3.It drives the browser effectively.
3.If there’s more than one element that matches the query, then only the first will be returned.
If nothing can be found, a NoSuchElementException will be raised.
'''
'''
The setUp method is part of initialization.
This method will get called before every test function which you are going to write in this test case class. 
Here you are creating an instance of a Firefox WebDriver.
-------------
driver = webdriver.Chrome(options=options)
##Options to describe the kind of session you want; default values are used for local, but this is required for 
remote
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

'''
The test case class is inherited from unittest.TestCase.
Inheriting from the TestCase class is the way to tell unittest module that this is a test case:
'''
class PythonOrgSearch(unittest.TestCase):

    '''
    The setUp method is part of initialization.
    This method will get called before every test function which you are going to write in this test case class.
    Here you are creating an instance of a Firefox WebDriver
    '''
    def setUp(self):
        self.driver = webdriver.Chrome()
    '''
    This is the test case method. The test case method should always start with characters test. 
    The first line inside this method creates a local reference to the driver object created in setUp method 
    '''
    def test_search_in_python_org(self):
        driver = self.driver
        '''
        The driver.get method will navigate to a page given by the URL. 
        WebDriver will wait until the page has fully loaded (that is, the “onload” event has fired) 
        before returning control to your test or script. 
        Be aware that if your page uses a lot of AJAX on load then WebDriver may not know when it has completely 
        loaded:
        '''
        driver.get("http://www.python.org")
        # The next line is an assertion to confirm that title has the word “Python” in it:
        self.assertIn("Python", driver.title)
        # WebDriver offers a number of ways to find elements using the find_element method.
        elem = driver.find_element(By.NAME, "q")
        # we are sending keys, this is similar to entering keys using your keyboard.
        # Special keys can be sent using the Keys class imported from selenium.webdriver.common.keys:
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)

    '''
    The tearDown method will get called after every test method. This is a place to do all cleanup actions. 
    In the current method, the browser window is closed. You can also call the quit method instead of close. 
    The quit method will exit the entire browser, whereas close will close a tab, 
    but if it is the only tab opened, by default most browsers will exit entirely
    '''
    def tearDown(self):
        self.driver.close()
'''
Final lines are some boiler plate code to run the test suite:
'''
if __name__ == "__main__":
    unittest.main()





# ------------------------------------
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# browser = webdriver.Firefox()
#
# browser.get('http://www.yahoo.com')
# assert 'Yahoo' in browser.title
#
# elem = browser.find_element(By.NAME, 'p')  # Find the search box
# elem.send_keys('seleniumhq' + Keys.RETURN)
#
# browser.quit()
# print("Success")
# ---------------------
# from selenium import webdriver
#
# driver = webdriver.Remote(
#    command_executor='http://127.0.0.1:4444/wd/hub',
#    options=webdriver.ChromeOptions()
# )

# ----------------------
import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.python.org")

    def test_search_in_python_org(self):
        """Tests python.org search feature. Searches for the word "pycon" then
        verified that some results show up.  Note that it does not look for
        any particular text in search results page. This test verifies that
        the results were not empty."""

        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        #Checks if the word "Python" is in title
        self.assertTrue(main_page.is_title_matches(), "python.org title doesn't match.")
        #Sets the text of search textbox to "pycon"
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty
        self.assertTrue(search_results_page.is_results_found(), "No results found.")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
'''
Page object classes:-
The page object pattern intends to create an object for each part of a web page. 
This technique helps build a separation between the test code and the actual code that interacts with the web page.

'''
