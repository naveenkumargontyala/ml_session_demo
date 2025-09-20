import math_utils

def test_sum():
    assert math_utils.add(2,3) == 5
    assert math_utils.add(-1,1) == 0
    assert math_utils.add(0,0) == 0
