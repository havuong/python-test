import pytest
from calc import my_divide

def test_divide():
    assert my_divide(6,3) == 2

def test_divide_by_negative():
    assert my_divide(-66,33) == -2

def test_divide_by_zero_exception():
    with pytest.raises(ZeroDivisionError): my_divide(-66,0)