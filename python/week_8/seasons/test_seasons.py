from seasons import inputd
from seasons import output
from pytest import raises
from datetime import date

def test_Invalid_date():
    with raises(ValueError):
        inputd("0-0-0")
    with raises(ValueError):
        inputd("200-2-30")
    with raises(ValueError):
        inputd("2000-5-35")

def test_Valid_output():
    assert(output(""))