from seasons import inputd
from seasons import output
from pytest import raises

def test_Invalid_date():
    with raises(SystemExit):
        inputd("2000-02-30")
    with raises(SystemExit):
        inputd("2000-5-35")

def test_Valid_output():
    assert(output("1995-01-01")) == "2629440"