import pytest
from tests import square

def main():
     test_square()


def test_square():
    assert square(2)==4
    assert square(3)==9

def test_negative():
    assert square(-2)==4
    assert square(-3)==9

def test_zero():
    assert square(0)==0

def test_str():
    with pytest.raises(TypeError):
        square("cat")
    

     
#    try: 
#        assert square(2)==4
#    except AssertionError:
#         print("2 square was not 4")

#    try:
#        assert square(-3)==9
#    except AssertionError:
#            print("-3 square was not 9")
    

#if __name__=="__main__":
#     main()