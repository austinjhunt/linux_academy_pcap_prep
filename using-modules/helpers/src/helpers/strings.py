#!/Users/huntaj/dev/pythoncertification/venv/bin/python3.7
"""Strings documentation for helpers package. """
# __all__ = [] defines what entities you want to be included in the following import statement:
# from module import *
# Will only affect from helpers import * statements.
# Explicit imports will still be able to import extract_lower, e.g. from helpers import extract_lower
# __all__ = ['extract_upper'] # So from helpers import * only imports extract_upper
# Alternative to this would be to prefix extract_lower with an _, e.g.

#pseudo-hidden entity, can still be explicitly imported, just not included in * imports

#def _extract_lower(phrase):
#    return list(filter(str.islower,phrase))
#
print(f"__name__ in helpers.py: {__name__}")
def extract_upper(phrase):
    """extract_upper takes a string and returns a list containing only the uppercase characters from the string

    Arguments:
        phrase {string} -- [phrase from which you want to extract upper]

    Returns:
        [list] -- [list of uppercase characters in phrase]
    This is a doctest. If you include what looks like REPL input and output, it acts as automated
    testing inside the documentation.
    >>> extract_upper("HELLo theRe BOB")
    ['H', 'E', 'L', 'L', 'R', 'B', 'O', 'B']
    """
    return list(filter(str.isupper,phrase))

def extract_lower(phrase):
    return list(filter(str.islower,phrase))
if __name__ == "__main__":
    print("Hello from helpers.")