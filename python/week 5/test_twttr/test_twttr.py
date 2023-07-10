from twttr import shorten

def test_vowels_lower():
    assert(shorten("Hello")) == "Hll"
    assert(shorten("Goodbye, World")) == "Gdby, Wrld"

def test_vowels_upper():
    assert(shorten("HELLO")) == "HLL"
    assert(shorten("GOODBYE, WORLD")) == "GDBY, WRLD"

def test_numbers():
    assert(shorten("I have 10 EURO")) == " hv 10 R"