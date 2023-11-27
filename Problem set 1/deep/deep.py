userip=input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
if (userip.strip() == '42' or userip.lower().strip() == "forty two" or userip.lower().strip() == "forty-two"):
    print('Yes')
else:
    print('No')

"""
txt.strip() -to remove spaces before and after the word.
txt.lower() -to make all letters lower case.

"""

