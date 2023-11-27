from fuel import convert, gauge
import pytest
#Test ZeroDivisionError
def test_zeroDivEr():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')

#Test ValueError
def test_val():
    with pytest.raises(ValueError):
        convert('cat/rat')

#Test Correct i/p.

def test_ip():
    assert convert('1/2')==50 and gauge(50)=='50%'
    assert convert('1/100')==1 and gauge(1)=='E'
    assert convert('99/100')==99 and gauge(99)=='F'