from numb3rs import validate

# Test if input is in format #.#.#.# where # is a number.

def test_input():
    assert validate(r'1.1.1.1') == True
    assert validate(r'1.1.1') == False
    assert validate(r'1.1') == False
    assert validate(r'1') == False
    assert validate(r'A.3.4.5') == False
    assert validate(r'2?3.5.6') == False

# Test if  number between 0 and 255, inclusive.
def test_limit():
    assert validate(r'255.255.255.255') == True
    assert validate(r'300.255.255.255') == False
    assert validate(r'255.300.255.255') == False
    assert validate(r'255.255.300.255') == False
    assert validate(r'255.255.255.300') == False
    assert validate(r'-300.255.255.255') == False
