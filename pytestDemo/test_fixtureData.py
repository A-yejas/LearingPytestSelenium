import pytest

@pytest.mark.usefixtures("dataload")
class TestExample2:
    '''
But here your scenario is different.
You want to actually return, you are returning something.
You are returning some data from your fixture.
In the previous topic.
We did not return anything so you can actually not required to pass as a parameter once you declare
globally.
But in this case you are returning something.
When you are returning, then it's mandatory to pass that fixture name into your method.
Okay, because you want to print something and this is where it works, right?
'''
    def test_editProfile(self,dataload):
        print(dataload)
        print(dataload[0])

from BaseClass import BaseClass
@pytest.mark.usefixtures("dataload")
class TestExample3(BaseClass):

    def test_logProfile(self,dataload):
        log = self.getLogger()
        log.info(dataload[0])
        log.info(dataload[2])
        # print(dataload)
        print(dataload[2])
