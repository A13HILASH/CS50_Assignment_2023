from twttr import shorten

def main():
    pass
#Test for case.
def test_case():
    assert shorten('twitter')=='twttr'
    assert shorten('TWITTER')=='TWTTR'
    assert shorten('TwTteR')=='TwTtR'
#Test numbers.
def test_num():
    assert shorten('1234')=='1234'
#Test special characters.
def test_spchar():
    assert shorten('?.,!@')=='?.,!@'
