import pytest

@pytest.mark.usefixtures("dataload")
class TestExample2:

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
