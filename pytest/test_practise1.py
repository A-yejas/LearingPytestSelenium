'''
 pytest --version
>>#Execute the test function with “quiet” reporting mode: pytest -q test_sysexit.py
#The -q/--quiet flag keeps the output brief in this and following examples.
--> those attributes added at class level are class attributes, so they will be shared between tests.
-------------------
1.When a fixture requests another fixture, the other fixture is executed first.
2.So if fixture a requests fixture b, fixture b will execute first, because a depends on b and can’t operate without it.
3.Even if a doesn’t need the result of b, it can still request b if it needs to make sure it is executed after b.
---------------------------
------------------------------How to invoke pytest
##Run tests by keyword expressions
Note:- This will run tests which contain names that match the given string expression (case-insensitive),
which can include Python operators that use filenames, class names and function names as variables.
***pytest -k 'MyClass and not method'
##To run a specific test within a module:
***pytest tests/test_mod.py::test_func
##To run all tests in a class:
***pytest tests/test_mod.py::TestClass
#Specifying a specific test method:
***pytest tests/test_mod.py::TestClass::test_method
##Specifying a specific parametrization of a test:
***pytest tests/test_mod.py::test_func[x1,y2]
------------Mark
Run tests by marker expressions
To run all tests which are decorated with the @pytest.mark.slow decorator:
***pytest -m slow
To run all tests which are decorated with the annotated @pytest.mark.slow(phase=1) decorator, with the phase keyword argument set to 1:
pytest -m "slow(phase=1)"
----Early loading plugins

pytest -p pytest_cov
---Disabling plugins
pytest -p no:doctest
Note:-To disable loading specific plugins at invocation time, use the -p option together with the prefix no:.
Example: to disable loading the plugin doctest, which is responsible for executing doctest tests from text files,
invoke pytest like this:
'''
###
'''
1.Using pytest.mark.xfail with the raises parameter is probably better for something like documenting unfixed bugs 
(where the test describes what “should” happen) or bugs in dependencies.
2.Using pytest.raises() is likely to be better for cases where you are testing exceptions your own code is 
deliberately raising, which is the majority of cases.
'''
#Defining your own explanation for failed assertions
'''
-->It is possible to add your own detailed explanations by implementing the pytest_assertrepr_compare hook.

pytest_assertrepr_compare(config, op, left, right):
Return explanation for comparisons in failing assert expressions.

Return None for no custom explanation, otherwise return a list of strings. The strings will be joined by newlines 
but any newlines in a string will be escaped. Note that all but the first line will be indented slightly, 
the intention is for the first line to be a summary.

Parameters:
config (Config) – The pytest config object.
op (str) – The operator, e.g. "==", "!=", "not in".
left (object) – The left operand.
right (object) – The right operand.
Use in conftest plugins
^^^^^^^^^^Filename - > pytest.ini
[pytest]
addopts = -p no:warnings

'''
# CHG :- Autouse fixtures (fixtures you don’t have to request)
#CHG :- usefixtures(
'''
SCOPE:- Possible values for scope are: function, class, module, package or session
@pytest.fixture(scope="module")
###To MAKE CONNECTION
# content of conftest.py
import smtplib
import pytest
@pytest.fixture(scope="module")
def smtp_connection():
    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)

----------------
###File Name:- content of test_module.py

def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert b"smtp.gmail.com" in msg
    assert 0  # for demo purposes


def test_noop(smtp_connection):
    response, msg = smtp_connection.noop()
    assert response == 250
    assert 0  # for demo purposes
------
@pytest.fixture(scope="session")
def smtp_connection():
    # the returned fixture value will be shared for
    # all tests requesting it
--------------------
Dynamic scope
def determine_scope(fixture_name, config):
    if config.getoption("--keep-containers", None):
        return "session"
    return "function"
@pytest.fixture(scope=determine_scope)
def docker_container():
    yield spawn_container()
'''
# def func(x):
#     return x+1
# def test_fun():
#     assert func(3) ==5
# And:- Failed assertion error func(3) does not return 5.
#You can use the assert statement to verify test expectations.
# ----------
#Execute the test function with “quiet” reporting mode: pytest -q test_sysexit.py
#The -q/--quiet flag keeps the output brief in this and following examples.
# import pytest
#
# def f():
#     raise SystemExit(1)
#
# def test_mytest():
#     with pytest.raises(SystemExit):
#         f()
# ------------
# content of test_exceptiongroup.py
# import pytest
#
# def f():
#     raise ExceptionGroup(
#         "Group message",
#         [
#             RuntimeError(),
#         ],
#     )
#
# def test_exception_in_group():
#     with pytest.raises(ExceptionGroup) as excinfo:
#         f()
    # assert excinfo.group_contains(RuntimeError)
    # assert not excinfo.group_contains(TypeError)
# ---------------
class TestClassDemoInstance:
    value = 0
    def test_one(self):
        self.value = 1
        assert self.value == 1
    def test_two(self):
        assert self.value == 1
# -----------------
'''
##Skip all test functions of a class or module
You can use the skipif marker (as any other marker) on classes:

@pytest.mark.skipif(sys.platform == "win32", reason="does not run on windows")
---------------
@pytest.mark.xfail(sys.platform == "win32", reason="bug in a 3rd party library")
-------
@pytest.mark.xfail(reason="known parser issue")
def test_function():
----------------
@pytest.mark.xfail(raises=RuntimeError)
def test_function():
----------
run parameter
If a test should be marked as xfail and reported as such but should not be even executed, use the run parameter as False:

@pytest.mark.xfail(run=False)
def test_function(): ...
This is specially useful for xfailing tests that are crashing the interpreter and should be investigated later.

strict parameter
Both XFAIL and XPASS don’t fail the test suite by default. You can change this by setting the strict keyword-only parameter to True:

@pytest.mark.xfail(strict=True)
def test_function(): ...
------
What is Scope:-
Pytest provides four levels of fixture scopes: Function (Set up and tear down once for each test function)
Class (Set up and tear down once for each test class)
Module (Set up and tear down once for each test module/file)
Session (Set up and tear down once for each test session i.e comprising one or more test files)
'''
# Plugins-pytest:-
'''
pytest-agent:-	
Service that exposes a REST API that can be used to interract remotely with Pytest. 
It is shipped with a dashboard that enables running tests in a more convenient way.
---
pytest-aggreport:-
pytest plugin for pytest-repeat that generate aggregate report of the same test cases with 
additional statistics details.
---------pytest (>=6.2.2)
-----------
pytest-allure-adaptor:-
Plugin for py.test to generate allure xml reports
-----pytest (>=2.7.3)
pytest-api :- 	
PyTest-API Python Web Framework built for testing purposes.






'''
# import keyword
#
# print(keyword.kwlist)
# ANS:-['False', 'None', 'True', 'and', 'as', 'assert',
#       'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
#       'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
#       'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
# ----


