#!/usr/bin/env python3.7


import sys
from .errors import ArgumentError

def main():
    if len(sys.argv) < 2:
        raise ArgumentError("Too few arguments")
    # Only use asserts in development and debugging because -O can be
    # passed during execution to optimize interpretation and that actually strips away
    # assert statements.
    assert len(sys.argv) >= 2, "Too few arguments"
    print(f"Name is {sys.argv[1]}")