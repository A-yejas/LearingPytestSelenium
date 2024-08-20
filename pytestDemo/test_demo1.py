'''
1.Any pytest file  should be start with test_ or end with _test
2.pytest method should sstart with test
3.Any code should be wrapped in method only
4.see that you have to give hyphen v(-v) stands for verbose that will give more information about logs.(output prints)
,v stands for verbose, which actually help you to give more information about your test case results.
4.default, console logs will not be shown in the output.If you want to show them, then you have to
again pass another flag called "-s" This is a flag which will help you to print all the console logs.All the console
logs in the output.
5.When you run this from test Runner, what this Pi charm provides, test runner automatically takes care
of all these flags by default.It will add all these.That's why you are seeing more information like
verbose and you are also seeing logs because test runner have these by default.
6.in pi test every method is treated as one test case.
7. we put one assertion this assert is part of pi test.It's just comparing two values based upon
true or false return.It will make test fall sorry, pass or fail.
8.in pi test you cannot have multiple test method names.With the same name.
If you have that, then it overrides the previous result.
9.Hyphen k "-k" stands for the specific regular expression whatever you are giving.
eg: pytest -k "partialfile"  this is how you can actually run selected module test cases.
10. -k stands for method names, execution -s for logs in output.
-v stands for more info like metadata.
We also saw you can run specific file.
pytest File name.
11.So let me add that you can Mark, (tag) test and then run with -m option.
ypu can Mark (tag) tests @pytest.nark.smoke and rn the file with -m
12.ypu can Mark (tag) tests @pytest.nark.skip
13.@pytest.mark.xfail when you give this, this particular test will run.
But in output you won't see about pass or fail.
So this is like just running but not reporting.
14.Data driven and parameterization.Can be done with return statements in tuple format.
15.When you define fixture scope to class only. It will run once before class is initiated.
After all the class methods are executed.
'''
import pytest


@pytest.mark.smoke
def test_demo1(test_first):
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Testing")

def test_first():
    print("-------------------Test1")
@pytest.mark.xfail
def test_creditcar():
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Test3")
#For Print tags  "python -m pytest -s -m  xfail .\test_demo1.py"

