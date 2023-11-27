from seasons import is_valid_date

def main():
    test_format()

def test_format():
    assert is_valid_date('199-11-11') == False
    assert is_valid_date('1999-1-11') == False
    assert is_valid_date('199-11-1') == False
    assert is_valid_date('January 1, 1999') == False

if __name__ == "__main__":
    main()