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
y0u can Mark (tag) tests @pytest.mark.smoke and rn the file with -m
RUN:- pytest -m tag_name(example:-smoke) -v -s
12.ypu can Mark (tag) tests @pytest.nark.skip
####But if you use skip, the complete test case is skipping and the operations, what you need for your
further test cases is also not happening at that time.
13.@pytest.mark.xfail when you give this, this particular test will run.
But in output you won't see about pass or fail.So this is like just running but not reporting and also wont appear in
console related that data.
---------
14.Data driven and parameterization.Can be done with return statements in tuple format.
15.When you define fixture scope to class only. It will run once before class is initiated.
After all the class methods are executed.
16.'pytest -k 'filename(function name) -s -v'
17.  ---> And you have some  Warnings in output after execution
What is this?
So they were saying that you have to register this marks(eg:marl.smoke) in your project.
Now smoke is the mark you defined, right?
18."conftest.py" That file you have to specifically define with that name only confest,.
This is the standard which you have to follow in that if yiu declared So in that file, if you declare your fixture,
then that fixture will be available to all the test files present in that specific folder.
19.Fixtures are used to set up and tear down methods.
Fixtures are used for setup and.It was the setup and teardown methods for test cases.Conf text file.
To.Generalize fixture.Feature and make it available to all test cases.
2.
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

