from jar import Jar
import pytest

def test_init():
    jar0 = Jar()
    assert jar0.capacity == 12
    jar1 = Jar(9)
    assert jar1.capacity == 9
    
    with pytest.raises (ValueError):
        jar2 = Jar(-2)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(9)
    assert jar.size == 9
    jar.deposit(2)
    assert jar.size == 11

    with pytest.raises (ValueError):
        jar.deposit(4)


def test_withdraw():
    jar = Jar()
    jar.deposit(9)
    jar.withdraw(3)
    assert jar.size == 6
    jar.withdraw(2)
    assert jar.size == 4
    
    with pytest.raises (ValueError):
        jar.withdraw(7)