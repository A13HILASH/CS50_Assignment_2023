from plates import is_valid
def main():
    pass
#Plates can contain max of 6 char and min of 2 char.
def test_min_max_char():
    assert is_valid('XX')==True
    assert is_valid('XXXXXX')==True
    assert is_valid('X')==False
    assert is_valid('XXXXXXXXXX')==False

#Plates should start with at least two letters.
def test_2lttr():
    assert is_valid('XX')==True
    assert is_valid('X1')==False
    assert is_valid('1X')==False
    assert is_valid('11')==False

#Numbers cannot be used in the middle of a plate; they must come at the end.
def test_num_in_middle():
    assert is_valid('XXX222')==True
    assert is_valid('XXX22X')==False

#First num used cannot be zero.
def test_num_zero():
    assert is_valid('XX10')==True
    assert is_valid('XX01')==False

#No periods, spaces, or punctuation marks are allowed.
def test_spchar():
    assert is_valid('XX3.14')==False
    assert is_valid('AB3&14')==False
    assert is_valid('VE3 14')==False