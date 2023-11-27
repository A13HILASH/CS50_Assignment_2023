from um import count
import pytest

def test_case():
    
    assert count('Um') == 1
    assert count('um') == 1

def test_substring():

    assert count('yummy') == 0
    assert count('Um, thanks for the album.') == 1

def test_space():

    assert count('Hey um how are you?') == 1


