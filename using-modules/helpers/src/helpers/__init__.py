"""
Helpers is a package that provides easy to user helper functions and variables.
"""


# This is where we put the initialization code for package.
__all__ = ['extract_upper']
from .strings import *


# Since python 3.3, implicit namespace packages
# you dont have to put __init__.py inside a package folder if the __init__.py
# is going to be empty. package will work exactly the same way.