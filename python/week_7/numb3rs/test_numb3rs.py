from numb3rs import validate

def test_correct():
    assert(validate("255.255.255.1")) is True
    assert(validate("1.2.3.4")) is True

def test_incorrect():
    assert(validate("2.256.2.7")) is False
    assert(validate("1000.6.400.2")) is False

def test_char():
    assert(validate("cat")) is False
    assert(validate("1.3.6.h.6")) is False