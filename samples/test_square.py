import math
import pytest 

@pytest.mark.square
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

@pytest.mark.square
def testsqare():
    num = 7
    assert 7 * 7 == 40

@pytest.mark.others
def testequality():
    assert 10 == 11