from NUMB3RS import validate


def test_valid():
    assert validate("192.168.1.1") == True
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True


def test_invalid():
    assert validate("275.3.6.28") == False
    assert validate("192.168.1") == False
    assert validate("192.168.1.256") == False


def test_letters():
    assert validate("cat.dog.1.1") == False
    assert validate("192.abc.1.1") == False


def test_extra():
    assert validate("192.168.1.1.1") == False
    assert validate("192.168.1.") == False
    assert validate(".192.168.1") == False