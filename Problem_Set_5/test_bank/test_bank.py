from bank import value
def main():
    pass
#Test if str starts with "hello".
def test_hello():
    assert value('hello')==0
    assert value('HELLO')==0
#Test if str starts with "h"(but not "hello").
def test_h():
    assert value('hey')==20
    assert value('HeY')==20
#Test for other str.
def test_str():
    assert value("sup")==100
    assert value("SUP")==100
