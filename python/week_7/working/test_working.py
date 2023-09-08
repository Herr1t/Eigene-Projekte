from working import convert
from pytest import raises

def test_time_r():
    assert(convert("9 AM to 5 PM")) == "09:00 to 17:00"
    assert(convert("9:00 AM to 5:00 PM")) == "09:00 to 17:00"
    assert(convert("11 PM to 12:34 AM")) == "23:00 to 00:34"

def test_time_w():
    with raises(ValueError):
        convert("123 PM to 1 AM")
    with raises(ValueError):
        convert("5:1 PM to 6:2 AM")
    with raises(ValueError):
        convert("9 AM - 5 PM")