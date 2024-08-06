import time

from selenium import  webdriver
'''
1. So our selenium webdriver will not directly invoke Chrome browser. "webdriver.Chrome()"Between these two 
there is something called Chrome Driver service.so this middleman plays a key role in invoking Chrome browser.
So basically Chrome browser will not give direct permission to any automation tools like selenium WebDriver.
to invoke and to perform actions.
If browser is not updated should go with chrome service get the stable chrome browser 
downlaod(downloaded and make sure you unzip okay.) add into you script.
eg:- Go first googlechromelab.github.com >> https://googlechromelabs.github.io/chrome-for-testing/) select 
stable driver from below options accordingly your bit-64 or 32 download and use
service_obj = Service(" latest downloaded path")
driver = webdriver.Chrome(service =service_obj)
So it comes as a zip extension.
You have to unzip and take that dot exe file.
So in windows you have to give like this.
You need to give with extension chrome driver dot exe.
If you are a windows user in Mac you don't need to give extension.
So in windows it starts with C users admin.
Wherever you put a path, take the path of that chrome driver and use dot exe in windows it is not required.
And then um once you create object for that service class hover your cursor import this um import.
You can say Chrome service.
This is important because you know you don't know right in your company what they offer.
So there is a class called service class okay.
So in this service class you have to give the path of the chrome driver what you just downloaded into
your system.
---
You know people might ask you in interview that what is Chrome driver.
What is its role in the whole execution.
And then you can explain and you can also explain how selenium inbuilt does that.
And if there are any issues faced, how you can encounter and how you can fix it with service class.
Okay, all this could be your, you know, um, questions where you can come across and you can give
'''
driver = webdriver.Chrome()
#service_obj=
driver.get('https://Rahulshettyacademy.com')
driver.maximize_window()
print(driver.current_url)
print(driver.title)
time.sleep(2)
