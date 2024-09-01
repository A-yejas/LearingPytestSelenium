'''
This file you have to specifically define with that name only.
"Conftest".
This is the standard which you have to follow.
Exactly to create this file.
So in this file, if you declare your fixture, then that fixture will be available to all the test
files present in that specific folder.
2. in this way we can reduce the code and make it more optimized by placing your fixtures in conf test.py
so in what scenario you have to place it, you have to place them in conf test only when you think that
particular fixture is shared by multiple files.
3.When you think that fixture is required by a number of files, then instead you can place it in one.
4.So if you want to make them run only once before the class and after all the test cases executed in
the class, then you need to simply go to your fixture argument where you have created in your config
test and here say scope equals to class.@pytest.fixture(scope="class")
5.Like if you put scope equals to class, then class level and if you don't put anything that will be
default applied on method level and the related annotations to set up pre and post conditions.
6.So as a precondition you can create one fixture, create all the data there, and then pass that fixture
into your test case so that data will be automatically available for your test case.
'''
import pytest
'''As I said in real time, you will use this particular block to invoke browser or to invoke some configuration'''
'''
if you put scope equals to class, then class level and if you don't put anything that will be
default applied on method level and the related annotations to set up pre and post conditions.
'''
@pytest.fixture(scope="class")
def test_first():
    print("This is First")
    '''properties and you will use this to close the browser and to delete the cookies at the end after your
test case execution is done.'''
    yield
    print("After second")

@pytest.fixture(scope="class")
def dataload():
    print("Something print data load fun")
    return ["Rahul","Sheety","rahulacademy@gamail.com"]

''' there is initial instance is "request for fixtures"'''
@pytest.fixture(params=[("chrome","Yejas","A"),("Firefox", "Ahamd"),("IE","SS")])
def crossbrowser(request):
    return request.param



