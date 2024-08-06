'''
1.in selenium framework we use this fixtures for opening a browser or setting up some database instances
or creating some configuration properties, environment variables.
It's all like prerequisite stuff.
Like if you want to run in Chrome browser, you will make sure you have Chrome driver setup and invoke
browser in this setup and then you start actual test cases inside it.
2. in py test if you put yield keyword then it automatically treats that whatever you write after this
yield step will be executed after your test execution is completed.
3.Fixtures are used as setup and teardown methods for test cases. -conftest file to Generalize fixture.
4.Feature and make it available to all test cases.

'''


def test_next(test_first):
    print("This is testing")
