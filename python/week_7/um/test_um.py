from um import count

def test_um():
    assert(count("Um, Hello, um, world.") == 2)
    assert(count("Um, thanks for the album.") == 1)
    assert(count("Uuum, i dont know, Um.") == 1)