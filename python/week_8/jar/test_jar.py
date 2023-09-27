from jar import Jar
from pytest import raises

def test_init():
    jar = Jar()
    assert jar.__init__()

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪🍪"
    jar.deposit(9)
    with raises(ValueError):
        str(jar)

def test_deposit():
    ...

def test_withdraw():
    ...