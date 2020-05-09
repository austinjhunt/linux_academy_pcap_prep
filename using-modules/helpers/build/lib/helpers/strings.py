#!/Users/huntaj/dev/pythoncertification/venv/bin/python3.7

# __all__ = [] defines what entities you want to be included in the following import statement:
# from module import *
# Will only affect from helpers import * statements.
# Explicit imports will still be able to import extract_lower, e.g. from helpers import extract_lower
# __all__ = ['extract_upper'] # So from helpers import * only imports extract_upper
# Alternative to this would be to prefix extract_lower with an _, e.g.
"""
pseudo-hidden entity, can still be explicitly imported, just not included in * imports

def _extract_lower(phrase):
    return list(filter(str.islower,phrase))
"""
print(f"__name__ in helpers.py: {__name__}")
def extract_upper(phrase):
    return list(filter(str.isupper,phrase))

def extract_lower(phrase):
    return list(filter(str.islower,phrase))
if __name__ == "__main__":
    print("Hello from helpers.")