from plates import is_valid

def test_len():
    assert(is_valid("G")) == False
    assert(is_valid("GHOLK34")) == False
    assert(is_valid("RTFG")) == True

def test_nonalpha_nonnumber():
    assert(is_valid("GH LK")) == False
    assert(is_valid("DF:+E")) == False

def test_begin_isalpha():
    assert(is_valid("2GJL")) == False
    assert(is_valid("73GDH")) == False
    assert(is_valid("G23")) == False

def test_enddigit():
    assert(is_valid("GHF22")) == True
    assert(is_valid("GHE2F")) == False

def test_begindigit():
    assert(is_valid("GHF02")) == False