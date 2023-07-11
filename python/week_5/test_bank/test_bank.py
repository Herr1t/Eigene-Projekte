from bank import value

def test_begin_h():
    assert(value(" hi")) == 20

def test_begin_hello():
    assert(value("Hello")) == 0

def test_no_h():
    assert(value("moin")) == 100