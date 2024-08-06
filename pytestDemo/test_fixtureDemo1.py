import pytest

'''
So when you give this, it will be automatically applied to all the methods present in your class so
you can get rid of passing the self.
So when you run this test now the fixture should apply pre request and post request and it should run accordingly.
'''

# @pytest.mark.usefixtures("test_first")
# class TestExample:
#     def test_demo1(self):
#         print("Testing1")
#
#     def test_demo2(self):
#         print("Testing2")
#
#     def test_demo3(self):
#         print("Testing3")
#
#     def test_demo4(self):
#         print("Testin4")
#
#     def test_demo5(self):
#         print("Testin5")
####
# Another Approach
'''
1.So if you want to run your fixer only once before the class, but not before each and every test case.
2.the class, then you need to simply go to your fixture argument where you have created in your config
test and here say scope equals to class.

'''
@pytest.mark.usefixtures("test_first")
class TestExample:
    def test_demo1(self):
        print("Testing1")

    def test_demo2(self):
        print("Testing2")

    def test_demo3(self):
        print("Testing3")

    def test_demo4(self):
        print("Testin4")

    def test_demo5(self):
        print("Testin5")
