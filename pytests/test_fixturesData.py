import pytest

@pytest.mark.usefixtures("dataLoad")
class TestExample2:

    def test_editProfile(self, dataLoad): #in what scenario u r forced to give fixtures name though u have declared globally?
        print(dataLoad[0])
        print(dataLoad[2])
