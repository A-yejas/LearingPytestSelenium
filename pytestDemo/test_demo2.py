import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("demo2 first program")

def test_creditdemo2program():
    print("This partial name preseent other file as well ")

'''
--> Fixture are make it available to all test cases (fixture name into parameters of method) 
Data driven and parameterization.Can be done with return statements in tuple format.
2.When you define fixture scope two class only. It will run once before class is initiated.
After all the class methods are executed.
3.pip install pytest-html
4.To generate reports :- pytest --html=report.html
selenium_new_release:-
service_obj= Service("path(ex:- chrome driver.exe)")
driver = webdriver.Chrome(service=service_obj)


And at the end.

'''
def test_crossbrowser(crossbrowser):
    print(crossbrowser[1])

