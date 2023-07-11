from fuel import convert
from fuel import gauge
from pytest import raises

def test_convert_int():
    with raises(ValueError):
        convert("a/7")
    with raises(ValueError):
        convert("10/9")
    assert(convert("2/4")) == 50
    assert(convert("2/3")) == 67

def test_convert_zero():
    with raises(ZeroDivisionError):
        convert("7/0")

def test_gauge_scase():
    assert(gauge(99)) == "F"
    assert(gauge(1)) == "E"

def test_gauge_output():
    assert(gauge(50)) == "50%"
    assert(gauge(67)) == "67%"