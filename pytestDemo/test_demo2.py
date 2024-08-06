import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("demo2 first program")

def test_creditdemo2program():
    print("This partial name preseent other file as well ")

'''
Data driven and parameterization.Can be done with return statements in tuple format.
2.When you define fixture scope two class only. It will run once before class is initiated.
After all the class methods are executed.

And at the end.

'''
def test_crossbrowser(crossbrowser):
    print(crossbrowser[1])

